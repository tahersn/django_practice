from django.contrib import admin


# Register your models here.
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib import messages



from .models import Event,participation
class ParticipateInline(admin.TabularInline):
    model = participation
    extra = 1
    readonly_fields = ['date']
    can_delete = False





class EventAdmin(admin.ModelAdmin):
    list_display = ('title','description','eventDate','satate','display_person_image')
    list_filter = ('title','eventDate')
    search_fields = ('title','description','eventDate','satate')
    ordering = ['title']
    actions = ['delete_selected','set_Accept']
    search_fields = [
        'title',
        'category'
    ]

    inlines = [ParticipateInline]
    def delete_selected(self, request, queryset):
        queryset.delete()
    delete_selected.short_description = "Delete selected events"

    def display_person_image(self, obj):
            if obj.image:
                return mark_safe('<img src="{}" width="100"  />'.format(obj.image.url))
            else:
                return '(No image)'

    display_person_image.short_description ='Person_Image'
    display_person_image.allow_tags = True
    def set_Accept(ModelAdmin, request, queryset):
    #set the state to 9rib
     rows = queryset.update(satate='9rib')
     if rows == 1:
        message = "One event was "
     else:
        message = f"{rows} events were"
     messages.success(request, message="% successfully accepted" % message)


admin.site.register(Event,EventAdmin)
admin.site.register(participation)
