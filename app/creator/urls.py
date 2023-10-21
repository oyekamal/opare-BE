from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CreatorQuestionViewSet, CreatorQuestionGroupingViewSet, CreatorRequestViewSet,
                    CreatorOutputViewSet, ConsolidatedQuestionsViewSet)

router = DefaultRouter()
router.register(r'creator_question', CreatorQuestionViewSet)
router.register(r'creator_question_grouping', CreatorQuestionGroupingViewSet)
router.register(r'creator_request', CreatorRequestViewSet)

router.register(r'creator_output', CreatorOutputViewSet)
router.register(r'consolidated_question', ConsolidatedQuestionsViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
