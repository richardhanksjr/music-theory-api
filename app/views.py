
from django.http import HttpResponse
from django.views import View


class TestRoute(View):
    def get(self, request):
        return HttpResponse("Successfully deployed from GitHub branch. Hey! This is Nathan checking in.")

