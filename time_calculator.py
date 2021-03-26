import time
from datetime import datetime, timedelta


def add_time(start, duration, weekDay=None):
    start_datetime = get_time_from_str(start)
    duration_time = get_hours_from_str(duration)
    new_time = calculate_time(start_datetime, duration_time)

    return convert_format(new_time, start_datetime, weekDay)


'''文字列から時刻 (datetime)を取得します'''


def get_time_from_str(start):
    base = time.strptime(start, "%I:%M %p")
    return datetime(*base[:6])


'''文字列から時間を取得します'''


def get_hours_from_str(hours):
    base = hours.split(':')
    total_minutes = int(base[0]) * 60 + int(base[1])
    return timedelta(hours=int(base[0]), minutes=int(base[1]))


'''時刻に時間を足して計算します'''


def calculate_time(base_time, hours):
    return base_time + hours


'''日付を文字列に変換します'''


def convert_format(result_time, start_datetime, weekDay=None):
    diff = result_time.date() - start_datetime.date()
    diff_days = diff.days

    result_string = result_time.strftime('%-I:%M %p')
    if (weekDay is not None):
        target_weekDay = get_weekDay(weekDay, diff_days)
        result_string = f'{result_string}, {target_weekDay}'

    if (diff_days == 1):
        return f'{result_string} (next day)'

    if (diff_days > 1):
        return f'{result_string} ({diff_days} days later)'
    return result_string


def get_weekDay(base_weekDay, dateDiff):
    weekDays = ("monday", "tuesday", "wednesday", "thursday", "friday",
                "saturday", "Sunday")
    wday = weekDays.index(base_weekDay.lower())
    targetWday = (wday + dateDiff) % 7
    result = weekDays[targetWday]
    return result.capitalize()
