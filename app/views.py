from django.http import HttpResponse
from django.views.generic import View


class TestRoute(View):
    def get(self, request):
        return HttpResponse("Successfully deployed from GitHub")