from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
class Student(view.View):
    def get(self, request):
        return HttpResponse("I am called from a get request")

    def post(self, request):
        return HttpResponse("I am called from a post request")

