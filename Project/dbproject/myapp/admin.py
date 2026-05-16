from django.contrib import admin
from .models import*



class stdata(admin.ModelAdmin):
    ordering=['id']
    list_display=["id","name","email"]

# Register your models here.
admin.site.register(studinfo,stdata)
