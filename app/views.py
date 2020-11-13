from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from questions.models import Tag, Question

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

class FilterPageView(LoginRequiredMixin, View):

    def get(self, request):
        tags = Tag.objects.all()
        return render(request, 'app/filter.html', {"tags": tags})

    # def post(self, request):
    #     chosen = request.POST.getlist('tag')
    #     if chosen:
    #
    #         print(chosen)
    #
    #         return render(request, 'app/filtered.html', {"chosen": chosen})
    #     else:
    #         chosen = "no items selected"
    #         print(chosen)
    #         return render(request, 'app/filtered.html', {"chosen": chosen})