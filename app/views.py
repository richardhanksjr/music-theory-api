from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# for all views, use LoginRequiredMixin


class LandingPageView(View):

    def get(self, request):
        return render(request, 'app/landing.html')
