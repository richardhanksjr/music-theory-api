import json
from django.shortcuts import render
from django.http import QueryDict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.cache import cache
from questions.question_generator import QuestionGenerator


class GetRandomQuestion(APIView):

    def get(self, request, format=None):
        question = QuestionGenerator.question_factory()
        print("from view", cache.get(question.key))
        data = question.response
        return Response(data)