from indoor_positioning.models import *
from django.db.models import QuerySet
from typing import List, TypedDict, Tuple, Dict, Optional, Union

__all__ = [
    'get_sensors',
    'fetch_sense_datas',
    'get_distances',
    'get_positions',
]

SensorData = TypedDict('dict', A=float, N=float, x=float, y=float)
Sensors = Dict[str, SensorData]
SenseData = QuerySet[SensedMobile]
Distance = Tuple[str, float]
Distances = List[Distance]
Point = Tuple[float, float]

def get_sensors(option: str='json') -> Sensors:
    '''获取id升序的嗅探器配置，option决定从何处获取值，可选值暂时只用json'''
    sensor_ids = WifiData.objects.order_by(
        'mobile_id').values_list('mobile_id', flat=True).distinct()
    # TODO: 增加其它数据
    sensors = {sensor_id: {} for sensor_id in sensor_ids}
    return sensors


def fetch_sense_datas(mobile_mac: str, sensors: Sensors,
                      max_count=1) -> List[Tuple[str, SenseData]]:
    '''获取指定设备最近的至多max_count条嗅探信息，更新到sensors中并返回列表'''
    sense_datas = []
    for sensor_id, sensor in sensors.items():
        sense_data = SensedMobile.objects.filter(
            sensor__mobile_id=sensor_id,
            mac=mobile_mac,
        ).order_by('-sensor__time')[:max_count]
        sensor.update(sense_data=sense_data)
        sense_datas.append((
            sensor_id,
            sense_data
        ))
    return sense_datas


def calculate_distance(sense_data: SensedMobile, sensor: SensorData,
                       option: str='rssi-mixed', **configs) -> float:
    ...


def get_distances(sensors: Sensors,
                  sense_datas: List[Tuple[str, SenseData]]=None,
                  **cal_kws) -> List[Distances]:
    '''
    计算每个时刻，目标点与每个嗅探器的距离。

    cal_kws被传递给calculate_distance
    当sense_datas为空时，使用sensors中的数据
    '''
    if sense_datas is None:
        ...
    sensors_list = [sensors[sd[0]] for sd in sense_datas]
    sense_datas_zip = zip(*[sd[1] for sd in sense_datas])
    for sense_data_zip in sense_datas_zip:
        for sensor, sense_data in zip(sensors_list, sense_data_zip):
            distance = calculate_distance(sense_data, sensor, **cal_kws)


def calculate_position(distances: Distances,
                       sensors: Sensors) -> Point:
    '''根据距离和嗅探器位置，计算某一时刻的坐标'''
    ...


def get_positions(distances_across_time: List[Distances],
                  sensors: Sensors) -> List[Point]:
    '''计算每个时刻，根据距离计算出的坐标'''
    return [calculate_position(distances, sensors)
            for distances in distances_across_time]
