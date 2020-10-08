from django.urls import path
from .views import GetRandomQuestion, Answer

app_name = 'api'

urlpatterns = [

    path('question', GetRandomQuestion.as_view(), name='random-question'),
    path('answer', Answer.as_view(), name='answer')

 ]