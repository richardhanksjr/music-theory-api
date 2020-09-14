from django.urls import path
from .views import TestRoute

urlpatterns = [
    path("", TestRoute.as_view(), name="test-route"),
]