"""Entrypoint script."""
import asyncio
from time import sleep

import schedule

import configuration as cfg
from get_data import get_data
from log2influxdb import Log2Influxdb
from log2mqtt import Log2MQTT
from logger import log


def _print_weather_data(data):
    """Print formmated weather data."""
    log_list = [f"{key[:4]}: {value}" for key, value in data.items()]
    log(" | ".join(log_list))


def _log_weather_data(mqtt_logger, influxdb_logger):
    """Log weather data."""
    data = asyncio.run(get_data())
    influxdb_logger.write_weather_point(data)
    mqtt_logger.log2topic(data)
    _print_weather_data(data)


def run():
    """Run the scheduler."""
    l2i = Log2Influxdb(host=cfg.INFLUXDB_HOST, database=cfg.INFLUXDB_DATABASE)
    l2m = Log2MQTT(host=cfg.MQTT_BROKER_URL, topic=cfg.MQTT_BROKER_TOPIC)

    schedule.every(cfg.JOB_MINUTES_INTERVAL).minutes.do(
        _log_weather_data, mqtt_logger=l2m, influxdb_logger=l2i)

    log(f"Scheduler started. Logging every {cfg.JOB_MINUTES_INTERVAL} minutes.")

    while True:
        try:
            log("Waiting for next job..")
            schedule.run_pending()
            sleep(30)
        except KeyboardInterrupt:
            log("Exiting..")
            break


if __name__ == "__main__":
    run()
