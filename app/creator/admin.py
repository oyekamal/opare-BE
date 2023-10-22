from django.contrib import admin

from .models import CreatorQuestion, CreatorQuestionGrouping, CreatorRequest, CreatorOutput, ConsolidatedQuestions


@admin.register(CreatorQuestion)
class CreatorQuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'short_name',
        'question_label',
        'help_text',
        'internal_description',
        'language',
        'creator_question_type',
        'creator_question_category',
        'user_input',
        'variable_type',
        'created_at',
        'updated_at',
    )
    list_filter = ('user_input', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(CreatorQuestionGrouping)
class CreatorQuestionGroupingAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(CreatorRequest)
class CreatorRequestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'short_name',
        'question_label',
        'user',
        'created_at',
        'updated_at',
    )
    list_filter = ('question_label', 'user', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(CreatorOutput)
class CreatorOutputAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'content',
        'label',
        'creator_request',
        'user',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'label',
        'creator_request',
        'user',
        'created_at',
        'updated_at',
    )
    date_hierarchy = 'created_at'


@admin.register(ConsolidatedQuestions)
class ConsolidatedQuestionsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'short_name',
        'creator_request',
        'user',
        'question',
        'created_at',
        'updated_at',
    )
    list_filter = ('creator_request', 'user', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'