from django.contrib import admin
from .models import Route, BusSchedule

class BusScheduleInline(admin.TabularInline):
    model = BusSchedule
    extra = 1

class RouteAdmin(admin.ModelAdmin):
    inlines = [BusScheduleInline]

admin.site.register(Route, RouteAdmin)
admin.site.register(BusSchedule)