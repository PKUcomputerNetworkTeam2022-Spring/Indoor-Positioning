from django.db import models
import json

# Create your models here.
class RawData(models.Model):
    """Raw sniffing data sent by the WIFI probe."""
    class Meta:
        verbose_name = '原始数据'
        verbose_name_plural = verbose_name
        ordering = ['-time']

    id = models.BigAutoField(primary_key=True)
    json_data = models.TextField('原数据')
    time = models.DateTimeField('创建时间', auto_now_add=True)

    @property
    def raw_data(self):
        return json.loads(self.json_data)

    @raw_data.setter
    def raw_data(self, val):
        self.json_data = json.dumps(val)


class WifiData(models.Model):
    """Sniffed data item."""
    class Meta:
        verbose_name = 'WiFi数据'
        verbose_name_plural = verbose_name

    id = models.BigAutoField(primary_key=True)
    sender_id = models.CharField('嗅探设备id', max_length=20)
    mobile_mac = models.CharField('MAC地址', max_length=20)
    rssi = models.FloatField('信号强度(rssi)')
    rssi1 = models.FloatField('rssi1', blank=True, null=True)
    rssi2 = models.FloatField('rssi2', blank=True, null=True)
    rssi3 = models.FloatField('rssi3', blank=True, null=True)
    rssi4 = models.FloatField('rssi4', blank=True, null=True)
    range = models.FloatField('测距距离(range)')
    raw_data = models.ForeignKey(RawData, on_delete=models.CASCADE)
