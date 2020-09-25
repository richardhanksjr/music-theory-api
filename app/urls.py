from django.urls import path
from .views import TestRoute
from django.views.generic import TemplateView

app_name = 'app'

urlpatterns = [
    path("", TestRoute.as_view(), name="test-route"),
    path("questions/", TemplateView.as_view(template_name='app/questions.html'), name="questions"),
]