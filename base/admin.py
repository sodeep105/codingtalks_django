from django.contrib import admin
from .models import Room, Topics, Message

# Register your models here.
admin.site.register(Room)
admin.site.register(Topics)
admin.site.register(Message)
