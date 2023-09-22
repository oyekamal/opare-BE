from django.contrib import admin

from .models import Question, Analyzer, QuestionInAnalyzer, Activity, Answer, KeyUsage

@admin.register(KeyUsage)
class KeyUsageAdmin(admin.ModelAdmin):
    list_display = (
        'api_key',
        'timestamp',
        'count',
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'short_name',
        'question',
        'created_at',
        'updated_at',
    )
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(Analyzer)
class AnalyzerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'analyzer_language',
        'analyzer_type',
        'analyzer_name',
        'analyzer_description',
        'analyzer_visibility',
        'created_at',
        'updated_at',
    )
    list_filter = ('created_at', 'updated_at')
    # raw_id_fields = ('analyzer_access',)
    date_hierarchy = 'created_at'


@admin.register(QuestionInAnalyzer)
class QuestionInAnalyzerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'analyzer',
        'is_displayed',
        'created_at',
        'updated_at',
    )
    list_filter = ('analyzer', 'is_displayed', 'created_at', 'updated_at')
    # raw_id_fields = ('question',)
    date_hierarchy = 'created_at'


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'created_at',
        'updated_at',
        'analyzer_language',
        'language',
        'is_universal',
        'is_visible',
        'private',
        'owner',
        'ai_answer',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'is_universal',
        'is_visible',
        'private',
        'owner',
        'ai_answer',
    )
    # raw_id_fields = ('analyzer',)
    date_hierarchy = 'created_at'


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'question',
        'activity',
        'analyzer',
        # 'answer',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'question',
        'activity',
        'analyzer',
        'created_at',
        'updated_at',
    )
    date_hierarchy = 'created_at'