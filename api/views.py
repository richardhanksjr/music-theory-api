from rest_framework.response import Response
from rest_framework.views import APIView
from questions.question_generator import QuestionGenerator


class GetRandomQuestion(APIView):

    def get(self, request):
        question = QuestionGenerator.question_factory()
        data = question.response
        return Response(data)