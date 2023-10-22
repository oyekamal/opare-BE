from rest_framework import serializers
from .models import CreatorQuestion, CreatorQuestionGrouping, CreatorRequest, CreatorOutput, ConsolidatedQuestions

class CreatorQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatorQuestion
        fields = '__all__'


class CreatorQuestionGroupingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatorQuestionGrouping
        fields = '__all__'
        depth = 1


class CreatorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatorRequest
        fields = '__all__'


class CreatorOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatorOutput
        fields = '__all__'


class ConsolidatedQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsolidatedQuestions
        fields = '__all__'