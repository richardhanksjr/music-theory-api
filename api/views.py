from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from questions.question_generator import QuestionGenerator


class GetRandomQuestion(APIView):

    def get(self, request, format=None):
        question = QuestionGenerator.question_factory()
        data = question.response
        return Response(data)