from .models import CreatorQuestion, CreatorQuestionGrouping, CreatorRequest, CreatorOutput, ConsolidatedQuestions

def replace_variable(questionLable: str, query) -> str:
    return questionLable.replace('<variable>', str(query)) + " \n"

def create_consolidated_question(data):
    core_question = ""
    for each_data in data:
        creator_question = CreatorQuestion.objects.get(id=each_data['id'])
        creator_output = CreatorOutput.objects.get(id=each_data['creator_output_id'])
        core_question += replace_variable(creator_question.question_label, creator_output.content)

    ConsolidatedQuestions.objects.create(short_name="test",question= core_question)
    return data
