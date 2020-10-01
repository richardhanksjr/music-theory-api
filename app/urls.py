
from django.urls import path

from django.views.generic import TemplateView

app_name = 'app'

urlpatterns = [
    path("questions/", TemplateView.as_view(template_name='app/questions.html'), name="questions"),
]
