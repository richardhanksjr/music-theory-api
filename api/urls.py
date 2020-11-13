from django.urls import path

from .views import GetRandomQuestion, Answer, HelpSteps, LogAttempt, Tags, TagsList

app_name = 'api'

urlpatterns = [

    path('question', GetRandomQuestion.as_view(), name='random-question'),
    path('answer', Answer.as_view(), name='answer'),
    path('help', HelpSteps.as_view(), name='help-steps'),
    path('attempt', LogAttempt.as_view(), name='attempt'),
    path('tags', TagsList.as_view(), name='tags-list' ),
    path('tags/<int:pk>/', Tags.as_view(), name='tags' )
 ]