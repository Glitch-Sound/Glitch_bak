import pytz                                     # type: ignore
from datetime import datetime, timedelta

from enum import Enum


class ItemType(Enum):
    PROJECT = 1
    EVENT   = 2
    FEATURE = 3
    STORY   = 4
    TASK    = 5
    BUG     = 6

class ItemState(Enum):
    IDLE     = 1
    RUN      = 2
    ALERT    = 3
    REVIEW   = 4
    COMPLETE = 5

class ExtractType(Enum):
    ALL          =  1
    INCOMPLETE   =  2
    HIGH_RISK    =  3
    ALERT        =  4
    ASSIGNMENT   =  5
    RELATION     =  6
    SEARCH       =  7
    PARENT       = 11
    SUMMARY_USER = 21

class TaskType(Enum):
    WORKLOAD = 1
    NUMBER   = 2


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
