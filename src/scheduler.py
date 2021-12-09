"""Entrypoint script."""
import asyncio
from datetime import datetime as dt
from time import sleep

import schedule

import configuration as cfg
from get_data import get_data
from log2influxdb import Log2Influxdb
from log2mqtt import Log2MQTT


def _print_weather_data(data):
    """Print formmated weather data."""
    log_list = [f"{key[:4]}: {value}" for key, value in data.items()]
    log_list.insert(0, f"{dt.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(" | ".join(log_list))


def _log_weather_data(mqtt_logger, influxdb_logger):
    """Log weather data."""
    data = asyncio.run(get_data())
    influxdb_logger.write_weather_point(data)
    mqtt_logger.log(data)
    _print_weather_data(data)


def run():
    """Run the scheduler."""
    l2i = Log2Influxdb(host=cfg.INFLUXDB_HOST, database=cfg.INFLUXDB_DATABASE)
    l2m = Log2MQTT(host=cfg.MQTT_BROKER_URL, topic=cfg.MQTT_BROKER_TOPIC)

    schedule.every(cfg.JOB_MINUTES_INTERVAL).minutes.do(
        _log_weather_data, mqtt_logger=l2m, influxdb_logger=l2i)

    while True:
        try:
            schedule.run_pending()
            sleep(10)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    run()
