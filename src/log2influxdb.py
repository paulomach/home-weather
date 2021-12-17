"""Log to influxdb."""
from datetime import datetime

from influxdb import InfluxDBClient


class Log2Influxdb:
    """Log to influxdb."""

    def __init__(self, host: str, database: str):
        """Initialize."""
        self.client = InfluxDBClient(host=host)
        self.client.create_database(database)
        self.client.switch_database(database)

    def write_weather_point(self, data: dict):
        """Log data."""
        json_body = [{
            "measurement": "weather",
            "tags": {
                "location": "home",

            },
            "time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "fields": {
                "temperature": float(data['temperature']),
                "cloud_cover": data['cloud_cover'],
                "radiation": data['radiation'],
            }
        }]

        self.client.write_points(json_body)


if __name__ == '__main__':
    import sys
    log2influxdb = Log2Influxdb(host=sys.argv[1], database=sys.argv[2])
    log2influxdb.write_weather_point({
        'temperature': 20.0,
        'cloud_cover': 50,
        'radiation': 10
    })
