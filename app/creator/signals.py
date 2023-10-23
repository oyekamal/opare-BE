from .models import ConsolidatedQuestions

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_q.tasks import async_task
from activity.ai_functions import activity_generate
from activity.models import Activity


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
