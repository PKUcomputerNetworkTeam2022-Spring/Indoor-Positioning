import json
import re

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from indoor_positioning.models import *
from indoor_positioning.utils import *


@csrf_exempt
def receiveData(request: HttpRequest):
    if request.method == 'POST' and request.POST.get('data') is not None:
        wifi_data: WifiData = WifiData.objects.create(json_data=request.POST['data'])
        for sensed_data in wifi_data.data:
            basic_infos = dict(
                sensor=wifi_data,
                mac=sensed_data['mac'],
                rssi=sensed_data['rssi'],
                range=sensed_data['range'],
                rssi1=sensed_data.get('rssi1'),
                rssi2=sensed_data.get('rssi2'),
                rssi3=sensed_data.get('rssi3'),
                rssi4=sensed_data.get('rssi4'),
            )
            if sensed_data.get('router') is not None:
                router_name: str = sensed_data['router']
                SensedRouter.objects.create(
                    device_name=router_name,
                    is_sensor=router_name.startswith('DataSky_f'),
                    **basic_infos,
                )
            else:
                tc = sensed_data.get('tc')
                if tc is None:
                    status = SensedMobile.Status.NOTCONNECTED
                else:
                    status = (
                        SensedMobile.Status.CONNECTED
                        if tc == 'Y' else
                        SensedMobile.Status.CONNECTING
                    )
                SensedMobile.objects.create(
                    status=status,
                    connected_ssid=sensed_data.get('ts'),
                    connected_mac=sensed_data.get('tmc'),
                    **basic_infos,
                )

    # 简单展示最后一条数据
    data = WifiData.objects.first()
    return render(request, 'receive.html', locals())


def showPosition(request: HttpRequest):
    if not request.GET.get('mobile_mac'):
        mobile_macs = SensedMobile.objects.order_by(
            'mac').values_list('mac', flat=True).distinct()
        return render(request, 'show_mobiles.html', {'mobiles': mobile_macs})

    mobile_mac = request.GET['mobile_mac']
    sensors = get_sensors()
    # 如果呈现多个时间点的坐标，修改max_count
    sense_datas = fetch_sense_datas(mobile_mac, sensors, max_count=1)
    distances_across_time = get_distances(sensors, sense_datas)
    positions = get_positions(distances_across_time, sensors)
    return render(request, 'show_position.html', locals())
