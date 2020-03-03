# encoding=utf-8

from rest_framework.serializers import ModelSerializer

from polls.models import Choice, Question


class QuestionSerializer(ModelSerializer):
    class Meta(object):
        model = Question
        fields = '__all__'


class ChoiceSerializer(ModelSerializer):
    class Meta(object):
        model = Choice
        fields = '__all__'
