from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from indoor_positioning.models import WifiData

# Create your views here.
@csrf_exempt
def receiveData(request: HttpRequest):
    if request.method == 'POST' and request.POST.get('data') is not None:
        WifiData.objects.create(json_data=request.POST['data'])

    # 简单展示最后一条数据
    data = WifiData.objects.first()
    return render(request, 'receive.html', locals())
