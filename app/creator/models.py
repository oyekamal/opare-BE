from django.db import models
from django.contrib.auth.models import User


LANGUAGES = (
    ('en', 'English'),
    ('fr', 'French'),
    ('es', 'Spanish'),
    # Add any other languages you need here
)


# class Desired(models.Model):
#     name = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


# class Creator(models.Model):
#     short_name = models.CharField(max_length=50)
#     desired = models.ForeignKey(Desired, on_delete=models.CASCADE)
#     language = models.CharField(max_length=2, choices=LANGUAGES, default='en')
#     number_of_students = models.IntegerField()
#     age = models.IntegerField()
#     grade = models.TextField()
#     course = models.TextField()
#     description = models.TextField()
#     teaching_intention = models.TextField()
#     learning_objectives = models.TextField()
#     duration = models.TextField()
#     educational_approach = models.TextField()
#     learning_approach_and_strategies = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class CreatorQuestionLabel(models.Model):
#     """
#     store information also add <variable> so the code does not break i.e
#     language: All the content must be writen and done in <variable>

#     """
#     language = models.TextField()
#     number_of_students = models.TextField()
#     age = models.TextField()
#     grade = models.TextField()
#     course = models.TextField()
#     description = models.TextField()
#     teaching_intention = models.TextField()
#     learning_objectives = models.TextField()
#     duration = models.TextField()
#     educational_approach = models.TextField()
#     learning_approach_and_strategies = models.TextField()
#     desired = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def save(self, *args, **kwargs):
#         # Check each field for '<variable>' value
#         fields = [f for f in self._meta.fields if isinstance(
#             f, (models.CharField, models.TextField))]
#         for field in fields:
#             value = getattr(self, field.name)
#             if '<variable>' not in value:  # Check if '<variable>' is in value
#                 # Update the field value and append '<variable>'
#                 setattr(self, field.name, value + '<variable>')
#         super().save(*args, **kwargs)

class CreatorQuestion(models.Model):
    short_name = models.CharField(max_length=255, default='short name')
    question_label = models.TextField(null=True)
    help_text = models.TextField(null=True)
    internal_description = models.TextField(null=True)
    language_choices = [
        ('en', 'English'),
        ('fr', 'French'),
        ('es', 'Spanish'),
    ]
    language = models.CharField(max_length=2, choices=language_choices, default='en', null=True)
    
    creator_question_types_choices = [
        ('output', 'Output'),
        ('global', 'Global'),
        ('detail', 'Detail'),
        ('transversal', 'Transversal'),
        ('specific', 'Specific'),
        ('item', 'Item'),
    ]
    creator_question_type = models.CharField(max_length=20, choices=creator_question_types_choices, default='output', null=True)

    creator_question_category_choices = [
        ('analyze', 'Analyze'),
        ('compose', 'Compose'),
        ('analyze_compose', 'Analyze and Compose'),
    ]
    creator_question_category = models.CharField(max_length=20, choices=creator_question_category_choices, default='analyze', null=True)
    
    user_input = models.BooleanField(null=True)
    
    variable_type_choices = [
        ('free_text', 'Free Text'),
        ('single_select', 'Single Select'),
        ('multi_select', 'Multi Select'),
        ('numerical_increment', 'Numerical Increment'),
        ('tag_multiselect', 'Tag Multiselect'),
    ]
    variable_type = models.CharField(max_length=20, choices=variable_type_choices, default='free_text', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.short_name

    def save(self, *args, **kwargs):
        # Check each field for '<variable>' value
        fields = [f for f in self._meta.fields if isinstance(
            f, (models.TextField))]
        for field in fields:
            if field.attname == 'question_label':
                value = getattr(self, field.name)
                if '<variable>' not in value:  # Check if '<variable>' is in value
                    # Update the field value and append '<variable>'
                    setattr(self, field.name, value + '<variable>')
        super().save(*args, **kwargs)


class CreatorQuestionGrouping(models.Model):
    short_name = models.CharField(max_length=255, default='short name')
    question = models.ManyToManyField(CreatorQuestion, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.short_name


class CreatorRequest(models.Model):
    short_name = models.CharField(max_length=255, default='')
    question_label = models.ForeignKey(
        CreatorQuestionGrouping, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.short_name


class CreatorOutput(models.Model):

    content = models.TextField()
    label = models.ForeignKey(CreatorQuestion, on_delete=models.CASCADE)
    creator_request = models.ForeignKey(
        CreatorRequest, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ConsolidatedQuestions(models.Model):
    """
    this model is responsable for storing Question created by above tables. and use for creating activity.
    """
    short_name = models.CharField(max_length=50)
    creator_request = models.ForeignKey(
        CreatorRequest, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.short_name