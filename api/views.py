from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin
from questions.question_generator import QuestionGenerator
from .serializers import TagSerializer
from questions.models import Attempt, Question, Tag
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import F


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
            data = cached_response['help_steps']
            expected_question_key = cached_response.get('key')
            if question_key != expected_question_key:
                return Response("The requested resource could not be found but may be available in the future.", status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response("Must supply question key", status=status.HTTP_400_BAD_REQUEST)
        return Response(data)

class LogAttempt(LoginRequiredMixin, APIView):
    def post(self, request):
        try:
            user_answer = request.data['answer']
            key = request.data['key']
            user = request.user
            cached_response = cache.get(key)
            class_name = cached_response['class_name']
            correct_answer = cached_response['answer']
            question_instance = get_object_or_404(Question, class_name=class_name)
            user_instance = get_object_or_404(User, username=user)
            user_correct = bool(user_answer == correct_answer)
            attempt = Attempt.objects.create(question=question_instance, user=user_instance, correct=user_correct)
            attempt.total_attempts = F('total_attempts') + 1
            attempt.save()
            if user_correct:
                attempt.number_correct = F('number_correct') + 1
                attempt.save()
            else:
                attempt.number_incorrect = F('number_incorrect') + 1
                attempt.save()

        except Exception:
            return Response("I'm sorry, we could not process your request", status=status.HTTP_400_BAD_REQUEST)
        return Response()

class TagsList(LoginRequiredMixin, ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class Tags(LoginRequiredMixin, RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer