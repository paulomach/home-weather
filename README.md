# home-weather

Log weather at given latitude/longitude using Solcast and WeatherAPI services
Log's to influxdb and mqtt queue for 3rd party consumption

## motivation

Toying around with my home automation setup

## Configuration

Configure with `.env` or export env vars as:

```shell
WEATHER_API_KEY=<your-weather-api-key>
WEATHER_API_URL="http://api.weatherapi.com/v1/current.json"

SOLAR_API_KEY=<your-solcast-api-key>
SOLAR_API_URL="https://api.solcast.com.au/world_radiation/estimated_actuals"

HOME_LATITUDE="<your-lat>"
HOME_LONGITUDE="<your-long>"
HOURS=7

MQTT_BROKER_URL="<a mqtt broker address>"
MQTT_BROKER_TOPIC="<a topic>"

INFLUXDB_HOST="<an influxdb address>"
INFLUXDB_DATABASE="<an influxdb database>"

JOB_MINUTES_INTERVAL=30
```

## Usage

Run scheduler script:

```shell
$ python src/scheduler.py
```

