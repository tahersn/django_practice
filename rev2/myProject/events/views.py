from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Event
#from .forms import EventForm, EventModelForm

# Create your views here.
def homePage(request):
    return HttpResponse('<h1><li><a href="/admin">Admin</a></li><li><a href="/list">List Events</a></li></h1>')

def listEvents(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events/listEvents.html', context)

def event_details(request,id):
    event =Event.objects.get(id=id)
    return render(
        request ,
        'events/eventDetails',
        {
            'event':event
        }
    )

    
                            
