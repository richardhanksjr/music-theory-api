from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from questions.question_generator import QuestionGenerator


class GetRandomQuestion(APIView):

    def get(self, request):
        question = QuestionGenerator.question_factory()
        data = question.response
        return Response(data)


class Answer(APIView):

    def post(self, request):
        try:
            user_answer = request.data['answer']
            answer_key = request.data['key']
            cached_response = cache.get(answer_key)
            data = {'correct': user_answer == cached_response['answer'],
                    'correct_answer': cached_response['answer']}
        except Exception:
            return Response("Must supply answer and key", status=status.HTTP_400_BAD_REQUEST)
        return Response(data)