"""Configuration retrival for container-based applications."""
import os

from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = os.getenv("WEATHER_API_URL")

SOLAR_API_KEY = os.getenv("SOLAR_API_KEY")
SOLAR_API_URL = os.getenv("SOLAR_API_URL")

HOME_LATITUDE = os.getenv("HOME_LATITUDE")
HOME_LONGITUDE = os.getenv("HOME_LONGITUDE")

HOURS = os.getenv("HOURS")

MQTT_BROKER_URL = os.getenv("MQTT_BROKER_URL")
MQTT_BROKER_TOPIC = os.getenv("MQTT_BROKER_TOPIC")

INFLUXDB_HOST = os.getenv("INFLUXDB_HOST")
INFLUXDB_DATABASE = os.getenv("INFLUXDB_DATABASE")

JOB_MINUTES_INTERVAL = int(os.getenv("JOB_MINUTES_INTERVAL"))
