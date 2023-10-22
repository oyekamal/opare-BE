from rest_framework import viewsets
from .models import CreatorQuestion, CreatorQuestionGrouping, CreatorRequest, CreatorOutput, ConsolidatedQuestions
from .serializers import (CreatorQuestionSerializer, CreatorQuestionGroupingSerializer, 
                          CreatorRequestSerializer, CreatorOutputSerializer,
                          ConsolidatedQuestionsSerializer)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework import status


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

    def create(self, request, *args, **kwargs):
        data = request.data  # Assuming the data is sent in the request body

        # Loop through the question data and create CreatorOutput instances
        for question_data in data['question']:
            creator_output_data = {
                'content': question_data['content'],
                'label': question_data['id'],  # Assuming 'id' corresponds to the 'label' ForeignKey
                # You may need to set other fields based on your requirements
            }
            serializer = CreatorOutputSerializer(data=creator_output_data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)


class ConsolidatedQuestionsViewSet(viewsets.ModelViewSet):
    queryset = ConsolidatedQuestions.objects.all()
    serializer_class = ConsolidatedQuestionsSerializer