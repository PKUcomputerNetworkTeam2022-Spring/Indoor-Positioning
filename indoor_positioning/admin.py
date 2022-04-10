from django.contrib import admin
from indoor_positioning.models import RawData, WifiData

# Register your models here.
@admin.register(RawData)
class DataAdmin(admin.ModelAdmin):
    list_display = ['id', 'time', 'json_data']
    list_filter = ['time']
    date_hierarchy = 'time'

@admin.register(WifiData)
class WifiDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender_id', 'mobile_mac', 'rssi', 'range', 'raw_data']
