from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Question(models.Model):
    short_name = models.CharField(max_length=255, default='short name')
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.short_name


class Analyzer(models.Model):
    LANGUAGES = (
        ('en', 'English'),
        ('fr', 'French'),
        ('es', 'Spanish'),
        # Add any other languages you need here
    )
    ANALYZER_TYPES = (
        ('universal', 'Universal'),
        ('curricular', 'Curricular'),
    )
    ANALYZER_VISIBILITY = (
        ('visible', 'Visible'),
        ('hidden', 'Hidden'),
        ('private', 'Private'),
    )
    analyzer_language = models.CharField(
        max_length=2, choices=LANGUAGES, default='en')
    analyzer_type = models.CharField(
        max_length=20, choices=ANALYZER_TYPES, default='universal')
    analyzer_name = models.CharField(max_length=255)
    analyzer_description = models.TextField(blank=True)
    analyzer_visibility = models.CharField(
        max_length=20, choices=ANALYZER_VISIBILITY, default='visible')
    analyzer_access = models.ManyToManyField(User, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Analyzers"

    def __str__(self):
        return self.analyzer_name


class QuestionInAnalyzer(models.Model):
    question = models.ManyToManyField(Question, blank=True)
    analyzer = models.OneToOneField(Analyzer, on_delete=models.CASCADE)
    is_displayed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "QuestionInAnalyzers"

    def __str__(self):
        return f"{self.analyzer.analyzer_name}"


class Activity(models.Model):
    LANGUAGES = (
        ('en', 'English'),
        ('fr', 'French'),
        ('es', 'Spanish'),
        # Add any other languages you need here
    )
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    analyzer_language = models.CharField(
        max_length=2, choices=LANGUAGES, default='en')
    analyzer = models.ManyToManyField(Analyzer, blank=True)
    language = models.CharField(max_length=2, choices=LANGUAGES, default='en')
    is_universal = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    private = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    ai_answer = models.BooleanField(default=False)
    file = models.FileField(upload_to='activities/', blank=True, null=True) # You can change the upload path as you wish
    url = models.URLField(blank=True, null=True)
    run_gpt = models.BooleanField(default=False)
    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('activity:activity_list')


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    analyzer = models.ForeignKey(Analyzer, on_delete=models.CASCADE)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.activity.title + " : " + self.question.question


class KeyUsage(models.Model):
    api_key = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField(default=0)

    def increment(self):
        self.count += 1
        self.save()

    def reset(self):
        self.count = 0
        self.save()

    def __str__(self):
        return f"{self.api_key} - {self.count}"