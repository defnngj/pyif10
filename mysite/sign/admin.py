from django.contrib import admin
from sign.models import Event, Guest


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ["name", "limit", "address", "start_time", "status"]
    search_fields = ["name", "address"]
    list_filter = ['status']


class GuestAdmin(admin.ModelAdmin):
    list_display = ["realname", "email", "phone", "sign"]
    search_fields = ["realname", "email", "phone"]
    list_filter = ['sign']


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
