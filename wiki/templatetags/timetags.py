import time
from django import template

register = template.Library()

def utime(timestamp):
    """Converts a timestamp in a formated time string"""
    try:
        ts = float(timestamp)
    except ValueError:
        return None

    return time.strftime("%H:%M:%S", time.gmtime(ts))

def udate(timestamp):
    """Converts a timestamp in a formated date string"""
    try:
        ts = float(timestamp)
    except ValueError:
        return None

    return time.strftime("%Y/%m/%d", time.gmtime(ts))

register.filter('unixdate', udate)
register.filter('unixtime', utime)
