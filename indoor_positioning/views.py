import json
import re

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from indoor_positioning.models import (SensedMobile, SensedRouter,
                                       SensedSenser, WifiData)


@csrf_exempt
def receiveData(request: HttpRequest):
    if request.method == 'POST' and request.POST.get('data') is not None:
        post_data = request.POST['data']
        wifi_data = WifiData.objects.create(json_data=post_data)
        post_data = json.loads(post_data, strict=False)
        for sensed_data in post_data['data']:
            mac = sensed_data.get('mac')
            rssi = sensed_data.get('rssi')
            range = sensed_data.get('range')
            rssi1, rssi2, rssi3, rssi4 = sensed_data.get('rssi1'), sensed_data.get(
                'rssi2'), sensed_data.get('rssi3'), sensed_data.get('rssi4')
            if 'router' in sensed_data:
                sensed_device = SensedSenser if re.search(
                    '^DataSky_f.*', sensed_data['router']) else SensedRouter
                sensed_device.objects.create(
                    senser=wifi_data,
                    mac=mac,
                    rssi=rssi,
                    range=range,
                    rssi1=rssi1,
                    rssi2=rssi2,
                    rssi3=rssi3,
                    rssi4=rssi4,
                    device_name=sensed_data.get('router'))
            else:
                tc = sensed_data.get('tc')
                if tc is None:
                    status = SensedMobile.Status.NOTCONNECTED
                else:
                    status = SensedMobile.Status.CONNECTED if tc == 'Y' else SensedMobile.Status.CONNECTING
                SensedMobile.objects.create(
                    senser=wifi_data,
                    mac=mac,
                    rssi=rssi,
                    range=range,
                    rssi1=rssi1,
                    rssi2=rssi2,
                    rssi3=rssi3,
                    rssi4=rssi4,
                    connected_ssid=sensed_data.get('ts'),
                    connected_mac=sensed_data.get('tmc'),
                    status=status)

    # 简单展示最后一条数据
    data = WifiData.objects.first()
    return render(request, 'receive.html', locals())
