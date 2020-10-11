from django.urls import path
from django.views.generic.base import TemplateView
from .views import LandingPageView, IndexPageView

app_name = 'app'

urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path("hello-vue", TemplateView.as_view(template_name="app/hello-vue.html"), name='hello-vue'),
    path("landing/", LandingPageView.as_view(), name="landing"),
]
