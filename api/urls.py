from django.urls import path
from .views import GetRandomQuestion, Answer, HelpSteps, Tags

app_name = 'api'

urlpatterns = [

    path('question', GetRandomQuestion.as_view(), name='random-question'),
    path('answer', Answer.as_view(), name='answer'),
    path('help', HelpSteps.as_view(), name='help-steps'),
    path('tags', Tags.as_view(), name='tags' ),
    path('tags/<int:pk>/', Tags.as_view(), name='tag' )
 ]