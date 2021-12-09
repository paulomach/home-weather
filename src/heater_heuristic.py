# TODO:
# implement some functional logic
#

"""Domain logic script."""
from datetime import datetime as dt



def warm_month():
    """Return True if it's a warm month."""
    return dt.now().month in [1, 2, 3, 9, 10, 11, 12]


def heat_temp_cover(temperature: float, cloud_cover: int):
    """
    Try to guess wheather should turn heater on for how long, based on temperature and cloud cover.

    Args:
        temperature (float): Temperature in Celsius
        cloud_cover (int): Cloud cover in %
    """
    if temperature < 0:
        return "cold"
    elif temperature < 10:
        return "warm"
    else:
        return "hot"


def heat_radiation(radiation: int):
    """
    Try to guess wheather should turn heater on for how long, based on radiation.

    Args:
        radiation (int): Radiation in W/m2
    """
    if radiation < 100:
        return "cold"
    elif radiation < 500:
        return "warm"
    else:
        return "hot"
