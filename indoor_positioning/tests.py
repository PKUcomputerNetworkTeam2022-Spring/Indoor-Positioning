import json
import string
import random
from datetime import datetime

# 为使IDE正常检测unittest，需要激活django环境
# 只依靠python manage.py test运行时则不需要以下三行
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'managing.settings')
django.setup()

from django.test import TestCase, Client
from indoor_positioning.models import WifiData, Data

# Create your tests here.
class ReceiveTestCase(TestCase):
    def setUp(self) -> None:
        self.device_id = "00f00000"
        self.mac = "00:ff:00:00:00:ff"
        self.sense_datas = (
            self.create_sense_datas()
            + self.create_router_datas()
        )
        self.send_time = datetime.strptime(datetime.now().strftime('%c'), '%c')
        self.raw_data = {
            "id": self.device_id,
            "mmac": self.mac,
            "rate": "5",
            "time": self.send_time.strftime('%c'),
            "lat": "",
            "lon": "",
            "data": self.sense_datas,
        }
        self.json_data = json.dumps(self.raw_data)
        self.response = Client().post('', {'data': self.json_data})
        self.insert_datas: WifiData = WifiData.objects.filter(
            mobile_id=self.device_id,
            mobile_mac=self.mac,
        )
        self.insert_data = self.insert_datas.first()
        return super().setUp()

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
        self.assertEqual(self.response.status_code, 200)

    def test_insert(self):
        self.assertIsNotNone(self.insert_data)

    def test_json_data(self):
        self.assertEqual(self.insert_data.json_data, self.json_data)

    def test_send_time(self):
        self.assertEqual(self.insert_data.time, self.send_time)
