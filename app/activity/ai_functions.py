import openai
from .models import Activity, Answer, Question, QuestionInAnalyzer, Analyzer, KeyUsage
from django.db.models import Min
openai.api_key = "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"

# openai.api_key = "org-CvXRMk8LiE3fDLcgmtJPOnBw"


def chunk_messages(messages, max_tokens):
    chunks = []

    for message in messages:
        # A rough estimate for token count
        message_tokens = len(message["content"])

        if message_tokens <= max_tokens:
            chunks.append([message])
        else:
            current_chunk = []
            current_tokens = 0

            for token in message["content"]:
                if current_tokens + 1 > max_tokens:
                    chunks.append(
                        [{"role": message["role"], "content": "".join(current_chunk)}])
                    current_chunk = []
                    current_tokens = 0

                current_chunk.append(token)
                current_tokens += 1

            if current_chunk:
                chunks.append(
                    [{"role": message["role"], "content": "".join(current_chunk)}])

    return chunks


def generate_summary(messages):
    summary_request = messages.copy()
    summary_request.append(
        {"role": "user", "content": "Please summarize the content in its original language."})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=summary_request
    )
    print("summarizing-content....!  PLEASE WAIT ")

    summary_response = completion.choices[0].message.content.strip()
    return summary_response


def ai_assistant(instance):
    print("ai_assistant called...!")
    messages = [
        {"role": "system", "content": "You’re a kind helpful assistant"}
    ]

    # Find the API key with the smallest count
    key_usage_with_min_count = KeyUsage.objects.annotate(
        min_count=Min('count')).first()

    # Increment the count for the selected API key
    key_usage_with_min_count.increment()
    key_usage_with_min_count.save()
    print("api_key ", key_usage_with_min_count.api_key)
    # Get the incremented API key
    openai.api_key = key_usage_with_min_count.api_key

    # Set up the prompt 2049
    max_tokens = 4097 - 100  # Leave some space for the assistant's response

    content = instance.content
    content_messages = [{"role": "user", "content": content}]
    content_chunks = chunk_messages(content_messages, max_tokens)

    summaries = []

    for content_chunk in content_chunks:
        summary = generate_summary(messages + content_chunk)
        summaries.append(summary)

    combined_summary = ' '.join(summaries)
    messages.append({"role": "user", "content": combined_summary})
    instance.summary = combined_summary

    for each_analyer in instance.analyzer.all():
        for each_questionset in QuestionInAnalyzer.objects.filter(analyzer=each_analyer):
            for each_question in each_questionset.question.all():
                question_message = {"role": "user",
                                    "content": each_question.question}
                messages.append(question_message)

                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                )

                chat_response = completion.choices[0].message.content
                print(f'ChatGPT: {chat_response}')
                response_message = {
                    "role": "assistant", "content": chat_response}
                messages.append(response_message)

                Answer.objects.update_or_create(
                    question=each_question, activity=instance, analyzer=each_analyer, answer=chat_response)

                # Remove the previous question and response from the messages list
                messages.remove(question_message)
                messages.remove(response_message)

        each_analyer.save()

    instance.ai_answer = True
    instance.run_gpt = False
    instance.save()


def activity_generate(data):
    question = data.get('question_text')
    if question:

        messages = [
            {"role": "system", "content": "Please create content."}
        ]

        # Find the API key with the smallest count
        key_usage_with_min_count = KeyUsage.objects.annotate(
            min_count=Min('count')).first()

        # Increment the count for the selected API key
        key_usage_with_min_count.increment()
        key_usage_with_min_count.save()
        print("api_key ", key_usage_with_min_count.api_key)
        # Get the incremented API key
        openai.api_key = key_usage_with_min_count.api_key

        # Set up the prompt 2049
        max_tokens = 4097 - 100  # Leave some space for the assistant's response

        content = question
        content_messages = [{"role": "user", "content": content}]
        content_chunks = chunk_messages(content_messages, max_tokens)

        summaries = []

        for content_chunk in content_chunks:
            summary = generate_summary(messages + content_chunk)
            summaries.append(summary)

        combined_summary = ' '.join(summaries)
        messages.append({"role": "user", "content": combined_summary})
        question_message = {"role": "user", "content": "created content"}
        messages.append(question_message)
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        chat_response = completion.choices[0].message.content
        data['activity'] = chat_response
        return data
