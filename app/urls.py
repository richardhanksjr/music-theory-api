from django.urls import path
from .views import LandingPageView, IndexPageView

app_name = 'app'
urlpatterns = [
    path("landing/", LandingPageView.as_view(), name="landing"),
    path("", IndexPageView.as_view(), name="index"),
]
