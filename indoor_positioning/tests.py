import json
import string
import random

# 为使IDE正常检测unittest，需要激活django环境
# 只依靠python manage.py test运行时则不需要以下三行
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'managing.settings')
django.setup()

from django.test import TestCase, Client
from indoor_positioning.models import WifiData, Data

# Create your tests here.
class ReceiveTestCase(TestCase):
    def rand_mac(self):
        return ':'.join(
            ''.join(random.choices(string.hexdigits[:16], k=2))
            for _ in range(6)
        )

    def create_sense_data(self, mac=None, rssi=None, rrange=None, **others):
        mac = mac or self.rand_mac()
        rssi = rssi or random.randint(-100, -30)
        rrange = rrange or random.randint(10, 1000) / 10
        return dict(
            mac=mac, rssi=str(rssi), range=str(rrange),
            **others,
        )

    def create_sense_datas(self, k=2):
        senser_datas = [
            self.create_sense_data()
            for _ in range(k)
            ]
        return senser_datas
    
    def create_router_data(self, mac=None, rssi=None, rrange=None, router=None, **others):
        router = router or random.choices(string.printable, k=random.randint(1, 10))
        return self.create_sense_data(mac, rssi, rrange, router=router, **others)

    def create_router_datas(self, k=5):
        routers = ["PKU", "PKU Visitor", "PKU Secure", "DataSky_f",]
        router_datas = [
            self.create_router_data(router=random.choice(routers))
            for _ in range(k)
        ]
        if k != 0:
            router_datas[0].update(tmc=self.rand_mac())
        return router_datas

    def create_mobile_data(self, mac=None, rssi=None, rrange=None, **others):
        raise NotImplementedError

    def create_mobile_datas(self, k=0):
        raise NotImplementedError

    def test_receive(self):
        c = Client()
        data = json.dumps({
            "id": "00f40444",
            "mmac": "14:6b:9c:f4:04:44",
            "rate": "5",
            "time": "Sat Apr 9 18:20:08 2022",
            "lat": "",
            "lon": "",
            "data": (
                self.create_sense_datas()
                + self.create_router_datas()
            ),
        })
        response = c.post('', {'data': data})
        self.assertEqual(response.status_code, 200)
        insert_data: WifiData = WifiData.objects.first()
        self.assertEqual(insert_data.json_data, data)
