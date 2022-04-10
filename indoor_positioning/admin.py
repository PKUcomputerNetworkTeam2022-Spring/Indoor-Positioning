from django.contrib import admin
from indoor_positioning.models import *

# Register your models here.
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['id', 'time', 'json_data']
    list_filter = ['time']
    date_hierarchy = 'time'


@admin.register(WifiData)
class WifiDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'mobile_id', 'mobile_mac', 'send_rate', 'time']
    list_filter = ['mobile_id', 'mobile_mac', 'time']
    date_hierarchy = 'time'


@admin.register(SensedDevice)
class SensedDeviceAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        admin.display(lambda x: x.sensor.mobile_id, description='嗅探器ID'),
        admin.display(lambda x: x.sensor.mobile_mac, description='嗅探器MAC'),
        'mac', 'rssi', 'range',
        admin.display(lambda x: x.sensor.time, description='发送时间'),
    ]
    list_filter = ['sensor__mobile_id', 'mac']
