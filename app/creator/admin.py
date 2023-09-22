from django.contrib import admin

from .models import Desired, Creator, CreatorQuestionLabel, ConsolidatedQuestions, CreatorQuestion, CreatorOutput, CreatorQuestionGrouping, CreatorRequest


@admin.register(Desired)
class DesiredAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'short_name',
        'desired',
        'language',
        'number_of_students',
        'age',
        'grade',
        'course',
        'description',
        'teaching_intention',
        'learning_objectives',
        'duration',
        'educational_approach',
        'learning_approach_and_strategies',
        'created_at',
        'updated_at',
    )
    list_filter = ('desired', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(CreatorQuestionLabel)
class CreatorQuestionLabelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'language',
        'number_of_students',
        'age',
        'grade',
        'course',
        'description',
        'teaching_intention',
        'learning_objectives',
        'duration',
        'educational_approach',
        'learning_approach_and_strategies',
        'desired',
        'created_at',
        'updated_at',
    )
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(ConsolidatedQuestions)
class CreatorQuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'short_name',
        'creator_question_label',
        'creator',
        'question',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'creator_question_label',
        'creator',
        'created_at',
        'updated_at',
    )
    date_hierarchy = 'created_at'


@admin.register(CreatorQuestion)
class CreatorQuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'short_name',
        'question_label',
        'created_at',
        'updated_at',
    )
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(CreatorOutput)
class CreatorOutputAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'label', 'created_at', 'updated_at')
    list_filter = ('label', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(CreatorQuestionGrouping)
class CreatorQuestionGroupingAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    # raw_id_fields = ('question',)
    date_hierarchy = 'created_at'


@admin.register(CreatorRequest)
class CreatorRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_name', 'question_label', 'created_at', 'updated_at')
    list_filter = ( 'created_at', 'updated_at')
    date_hierarchy = 'created_at'