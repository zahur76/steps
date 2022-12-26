from django.contrib import admin

# Register your models here.
from .models import Steps

class StepsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "steps")


admin.site.register(Steps, StepsAdmin)
