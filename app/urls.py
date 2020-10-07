from django.urls import path
from .views import LandingPageView, IndexPageView, ProfilePageView

app_name = 'app'
urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path("landing/", LandingPageView.as_view(), name="landing"),
    path("profile/", ProfilePageView.as_view(), name="profile"),
]
