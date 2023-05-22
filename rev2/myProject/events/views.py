from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Event
#from .forms import EventForm, EventModelForm

# Create your views here.
def homePage(request):
    return HttpResponse('<h1>Welcome To... </h1>')
