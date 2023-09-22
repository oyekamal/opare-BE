from .models import ConsolidatedQuestions, Creator, CreatorQuestionLabel

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_q.tasks import async_task
from activity.ai_functions import activity_generate
from activity.models import Activity


def replace_variable(questionLable: str, query) -> str:
    return questionLable.replace('<variable>', str(query)) + " \n"


@receiver(post_save, sender=Creator)
def Creator_saved(sender, instance, **kwargs):

    # if instance and kwargs.get('created'):
    if instance:
        print(instance)
        # create Question
        question_label = CreatorQuestionLabel.objects.all().first()
        question_text = ""

        question_text += replace_variable(question_label.desired,
                                          instance.desired.name)
        question_text += replace_variable(question_label.language,
                                          instance.language)
        question_text += replace_variable(
            question_label.number_of_students, instance.number_of_students)
        question_text += replace_variable(question_label.age, instance.age)
        question_text += replace_variable(question_label.grade, instance.grade)
        question_text += replace_variable(question_label.course,
                                          instance.course)
        question_text += replace_variable(
            question_label.description, instance.description)
        question_text += replace_variable(
            question_label.teaching_intention, instance.teaching_intention)
        question_text += replace_variable(
            question_label.learning_objectives, instance.learning_objectives)
        question_text += replace_variable(question_label.duration,
                                          instance.duration)
        question_text += replace_variable(
            question_label.educational_approach, instance.educational_approach)
        question_text += replace_variable(question_label.learning_approach_and_strategies,
                                          instance.learning_approach_and_strategies)

        ConsolidatedQuestions.objects.create(short_name=instance.short_name,
                                       creator_question_label=question_label,
                                       creator=instance,
                                       question=question_text)

        # activity = activity_generate(question_text)

        # Activity.objects.create(title=instance.short_name + ": activity",
        #                         description=activity, language=instance.language)

def call_back(task):
    
    print("Activity created..!")
    Activity.objects.create(title=task.result.get("short_name"),
                                content=task.result.get("activity"),
                                owner=task.result.get("user"))
    
@receiver(post_save, sender=ConsolidatedQuestions)
def creator_question_signal(sender, instance, **kwargs):
    # if instance and kwargs.get('created'):
    if instance:
        question_text = instance.question

        data = {
            "question_text":question_text,
            "short_name": instance.short_name + ": activity",
            "user": instance.user
        }
        async_task(activity_generate, data, hook=call_back)
