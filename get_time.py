from time import sleep
from datetime import datetime


def get_hour(hour):
    now = hour
    current = 0
    result = 0
    if now != current:
        current = now
        if now % 2 == 0:
            result = 0
        else:
            result = 1
    return result
