from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin
from questions.question_generator import QuestionGenerator


class GetRandomQuestion(LoginRequiredMixin, APIView):

    def get(self, request):
        question = QuestionGenerator.question_factory()
        data = question.response
        return Response(data)


class Answer(LoginRequiredMixin, APIView):

    def post(self, request):
        try:
            user_answer = request.data['answer']
            answer_key = request.data['key']
            user = request.user
            cached_response = cache.get(answer_key)
            expected_user_id = cached_response.get('user_id')
            if expected_user_id and expected_user_id != user.id:
                return Response("User does not have permission to view this answer", status=status.HTTP_403_FORBIDDEN)
            data = {'correct': user_answer == cached_response['answer'],
                    'correct_answer': cached_response['answer']}
        except Exception:
            return Response("Must supply answer and key", status=status.HTTP_400_BAD_REQUEST)
        return Response(data)

class HelpSteps(LoginRequiredMixin, APIView):

    def post(self, request):
        try:
            question_key = request.data['key']
            cached_response = cache.get(question_key)
            data = {'help_steps': cached_response['help_steps']}
            expected_question_key = cached_response.get('key')
            if question_key != expected_question_key:
                return Response("The requested resource could not be found but may be available in the future.", status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response("Must supply question key", status=status.HTTP_400_BAD_REQUEST)
        return Response(data)