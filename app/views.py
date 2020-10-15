from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# for all views that require user to be logged in, use LoginRequiredMixin


class LandingPageView(View):

    def get(self, request):
        return render(request, 'app/landing.html')

class IndexPageView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'app/questions.html')

class ProfilePageView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'app/profile.html')