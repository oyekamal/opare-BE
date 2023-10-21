from rest_framework import viewsets
from .models import CreatorQuestion, CreatorQuestionGrouping, CreatorRequest, CreatorOutput, ConsolidatedQuestions
from .serializers import (CreatorQuestionSerializer, CreatorQuestionGroupingSerializer, 
                          CreatorRequestSerializer, CreatorOutputSerializer,
                          ConsolidatedQuestionsSerializer)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class CreatorQuestionViewSet(viewsets.ModelViewSet):
    queryset = CreatorQuestion.objects.all()
    serializer_class = CreatorQuestionSerializer


class CreatorQuestionGroupingViewSet(viewsets.ModelViewSet):
    queryset = CreatorQuestionGrouping.objects.all()
    serializer_class = CreatorQuestionGroupingSerializer


class CreatorRequestViewSet(viewsets.ModelViewSet):
    queryset = CreatorRequest.objects.all()
    serializer_class = CreatorRequestSerializer


class CreatorOutputViewSet(viewsets.ModelViewSet):
    queryset = CreatorOutput.objects.all()
    serializer_class = CreatorOutputSerializer


class ConsolidatedQuestionsViewSet(viewsets.ModelViewSet):
    queryset = ConsolidatedQuestions.objects.all()
    serializer_class = ConsolidatedQuestionsSerializer