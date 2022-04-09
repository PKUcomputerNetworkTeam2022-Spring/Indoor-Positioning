from django.contrib import admin
from indoor_positioning.models import Data, WifiData

# Register your models here.
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['id', 'time', 'json_data']
    list_filter = ['time']
    date_hierarchy = 'time'

@admin.register(WifiData)
class WifiDataAdmin(DataAdmin):
    pass