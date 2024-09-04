import pytz                                     # type: ignore
from datetime import datetime, timedelta

def getPreviousDate():
    current_utc_time = datetime.now(pytz.timezone('Asia/Tokyo'))
    previous_date_time = current_utc_time - timedelta(days=1)
    previous_date = previous_date_time.strftime('%Y-%m-%d')
    return previous_date

def getCurrentDate():
    current_utc_time = datetime.now(pytz.timezone('Asia/Tokyo'))
    current_date = current_utc_time.strftime('%Y-%m-%d')
    return current_date


def getCurrentDatetime():
    current_utc_time = datetime.now(pytz.timezone('Asia/Tokyo'))
    current_datetime = current_utc_time.strftime('%Y-%m-%d %H:%M:%S')
    return current_datetime
