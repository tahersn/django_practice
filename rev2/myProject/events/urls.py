from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name='homePage'),
    path('list/', listEvents, name='listEvents'),
    path('Details/<int:id>',event_details, name='eventDetails')
]