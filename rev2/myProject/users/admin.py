from django.contrib import admin

# Register your models here.
from .models import Person

class personAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person)
