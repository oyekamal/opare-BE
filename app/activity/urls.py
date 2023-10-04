from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, AnalyzerViewSet, AnswerViewSet

router = DefaultRouter()
router.register(r'activities', ActivityViewSet)
router.register(r'analyzer', AnalyzerViewSet)
router.register(r'answers', AnswerViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
