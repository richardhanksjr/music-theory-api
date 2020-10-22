from django.urls import path
from .views import GetRandomQuestion, Answer, HelpSteps

app_name = 'api'

urlpatterns = [

    path('question', GetRandomQuestion.as_view(), name='random-question'),
    path('answer', Answer.as_view(), name='answer'),
    path('help', HelpSteps.as_view(), name='help-steps')
 ]