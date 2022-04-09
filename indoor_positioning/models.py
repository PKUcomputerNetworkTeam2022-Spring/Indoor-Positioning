from django.db import models
import json

# Create your models here.
class Data(models.Model):
    class Meta:
        verbose_name = '数据'
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


class WifiData(Data):
    class Meta:
        verbose_name = 'WiFi数据'
        verbose_name_plural = verbose_name

    mobile_id = models.CharField('嗅探器ID', max_length=15)
    mobile_mac = models.CharField('嗅探器MAC地址', max_length=20)
    send_rate = models.IntegerField('发送频率')
    latitude = models.FloatField('维度', blank=True, null=True)
    longitude = models.FloatField('精度', blank=True, null=True)

    @property
    def data(self):
        return self.raw_data['data']

    def set_default(self, **field_values):
        raw_data = None
        for field, from_field in field_values.items():
            if getattr(self, field) is None:
                if raw_data is None:
                    # lazy load
                    raw_data = self.raw_data or {}
                try:
                    if isinstance(from_field, (list, tuple)):
                        from_field, cast = from_field
                        setattr(self, field, cast(raw_data.get(from_field)))
                    else:
                        setattr(self, field, raw_data.get(from_field))
                except:
                    pass
    
    def save(self, *args, **kwargs) -> None:
        self.set_default(
            mobile_id='id',
            mobile_mac='mmac',
            send_rate='rate',
            latitude=['lat', float],
            longitude=['lon', float],
        )
        return super().save(*args, **kwargs)
