from django.contrib import admin

from .models import Todo, Client

admin.site.register(Todo) 
admin.site.register(Client)