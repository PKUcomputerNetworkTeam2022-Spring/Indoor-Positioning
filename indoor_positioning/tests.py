import json
import random
import string
from datetime import datetime

# 为使IDE正常检测unittest，需要激活django环境
# 只依靠python manage.py test运行时则不需要以下四行
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'managing.settings')
django.setup()

from django.test import TestCase

from indoor_positioning.models import *


# Create your tests here.
class ReceiveTestCase(TestCase):
    def setUp(self) -> None:
        self.device_id = "00f00000"
        self.mac = self.rand_mac()
        self.sensor_count = 0
        self.router_count = 5
        self.mobile_count = {status: 1 for status in SensedMobile.Status}
        self.sense_datas = (
            [self.create_router_data(router='DataSky_f00000', rrange=1.0)]
            + self.create_router_datas()
            + self.create_mobile_datas()
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
        self.response = self.client.post('', {'data': self.json_data})
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

    def create_router_data(self, mac=None, rssi=None, rrange=None, router=None, **others):
        router = router or random.choices(string.printable, k=random.randint(1, 10))
        return self.create_sense_data(mac, rssi, rrange, router=router, **others)

    def create_router_datas(self):
        routers = ["PKU", "PKU Visitor", "PKU Secure"]
        router_datas = [
            self.create_router_data(router=random.choice(routers))
            for _ in range(self.router_count)
        ]
        if self.router_count != 0:
            router_datas[0].update(tmc=self.rand_mac())
        return router_datas

    def create_mobile_data(self, mac=None, rssi=None, rrange=None,
                           status=SensedMobile.Status.NOTCONNECTED,
                           ts_choices=[''],
                           **others):
        if status == SensedMobile.Status.NOTCONNECTED:
            return self.create_sense_data(mac, rssi, rrange, **others)
        return self.create_mobile_data(
            ts=random.choice(ts_choices), tmc=self.rand_mac(),
            tc='Y' if status == SensedMobile.Status.CONNECTED else 'N',
        )

    def create_mobile_datas(self):
        ts_choices = ["PKU", "PKU Visitor", "PKU Secure", "DataSky_f"]
        mobile_datas = []
        for status, count in self.mobile_count.items():
            mobile_datas.extend([
                self.create_mobile_data(status=status, ts_choices=ts_choices)
                for _ in range(count)
            ])
        return mobile_datas

    def test_receive(self):
        self.assertEqual(self.response.status_code, 200)

    def test_insert(self):
        self.assertIsNotNone(self.insert_data)

    def test_json_data(self):
        self.assertEqual(self.insert_data.json_data, self.json_data)

    def test_send_time(self):
        self.assertEqual(self.insert_data.time, self.send_time)

    def test_sense_sensor(self):
        self.assertEqual(
            SensedRouter.objects.filter(
                sensor=self.insert_data,
                is_sensor=True,
            ).count(), self.sensor_count + 1,
        )

    def test_sense_router(self):
        self.assertEqual(
            SensedRouter.objects.filter(
                sensor=self.insert_data,
                is_sensor=False,
            ).count(), self.router_count,
        )

    def test_sense_mobile(self):
        for status, count in self.mobile_count.items():
            self.assertEqual(
                SensedMobile.objects.filter(
                    sensor=self.insert_data,
                    status=status,
                ).count(), count, status
            )
