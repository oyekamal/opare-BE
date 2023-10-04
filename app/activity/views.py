from rest_framework import viewsets
from .models import Activity, Analyzer, Answer
from .serializers import ActivitySerializer, AnalyzerSerializer, AnswerSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class AnalyzerViewSet(viewsets.ModelViewSet):
    queryset = Analyzer.objects.all()
    serializer_class = AnalyzerSerializer
    

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        'question__short_name': ['exact'],
        'activity__title': ['exact'],
        'analyzer__analyzer_name': ['exact'],
        # Add more filters as needed
    }
    ordering_fields = ['created_at', 'updated_at']  # Specify fields for ordering
    ordering = ['-created_at']  # Default ordering
