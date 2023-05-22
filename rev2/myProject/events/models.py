import datetime
from django.db import models
from django.forms import ValidationError
from users.models import Person

def eventDateValidator(value):
    if value < datetime.date.today():
        raise ValidationError('Invalid date - event is in the past')

    

CATEG_CHOICES = (
    ('MUSIC', 'MUSIC'),
    ('SPORT', 'SPORT'),
    ('ART', 'ART'),)

# Create your models here.
class Event (models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(choices=CATEG_CHOICES, max_length=200)
    satate = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    nbrParticipants = models.IntegerField(default=0)
    eventDate = models.DateField(validators=[eventDateValidator])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    # def __str__(self):
    #     return self.title
    
    participate = models.ManyToManyField(Person,related_name='participations',through='Participation')

class participation (models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    

    class Meta:
        unique_together = ('person', 'event')    
    
    

