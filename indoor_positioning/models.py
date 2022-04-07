from django.db import models
import json

# Create your models here.
class Data(models.Model):
    class Meta:
        verbose_name = '数据'
        verbose_name_plural = verbose_name
        ordering = ['-time']

    id = models.BigAutoField(primary_key=True)
    raw_data = models.TextField('原数据')
    time = models.DateTimeField('创建时间', auto_now_add=True)

    @property
    def data(self):
        return json.loads(self.raw_data)

    @data.setter
    def data(self, val):
        self.raw_data = json.dumps(val)


class WifiData(Data):
    class Meta:
        verbose_name = 'WiFi数据'
        verbose_name_plural = verbose_name
