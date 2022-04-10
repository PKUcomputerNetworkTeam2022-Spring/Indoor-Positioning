import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from indoor_positioning.models import WifiData, RawData

# Create your views here.


@csrf_exempt
def receiveData(request: HttpRequest):
    if request.method == 'POST' and request.POST.get('data') is not None:
        post_data = request.POST['data']
        raw_data = RawData(json_data=post_data)
        raw_data.save()
        post_data = json.loads(post_data, strict=False)
        probe_id = post_data['id']
        for wifi_data in post_data['data']:
            WifiData.objects.create(
                sender_id=probe_id,
                mobile_mac=wifi_data.get('mac'),
                rssi=wifi_data.get('rssi'),
                range=wifi_data.get('range'),
                rssi1=wifi_data.get('rssi1'),
                rssi2=wifi_data.get('rssi2'),
                rssi3=wifi_data.get('rssi3'),
                rssi4=wifi_data.get('rssi4'),
                raw_data=raw_data)

    # 简单展示最后一条原始数据
    data = RawData.objects.first()
    return render(request, 'receive.html', locals())
