from django.urls import path
from .views import LandingPageView, IndexPageView, ProfilePageView
from django.views.generic.base import TemplateView


app_name = 'app'

urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path("landing/", LandingPageView.as_view(), name="landing"),
    path("profile/", ProfilePageView.as_view(), name="profile"),
    path("hello-vue", TemplateView.as_view(template_name="app/hello-vue.html"), name='hello-vue'),
]
