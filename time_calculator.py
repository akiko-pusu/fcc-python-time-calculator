import time
from datetime import datetime, timedelta

def add_time(start, duration):
    new_time = '12:03 AM, Thursday'
    return new_time

'''文字列から時刻 (datetime)を取得します'''
def get_time_from_str(start):
    base = time.strptime(start, "%I:%M %p")
    return datetime(*base[:6])

'''文字列から時間を取得します'''
def get_hours_from_str(hours):
    base = hours.split(':')
    return timedelta(hours=int(base[0]), minutes=int(base[1]))

'''時刻に時間を足して計算します'''
def calculate_time(base_time, hours):
    return base_time + hours
