from django.contrib import admin

from .models import Agent, FuzzingTarget


# Register your models here.


admin.site.register(Agent)
admin.site.register(FuzzingTarget)
