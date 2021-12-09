"""Async data retrieval functions."""
import asyncio

import configuration as cfg
import solar_query
import weather_query


def _configure_objects() -> tuple:
    """Configure objects for queries."""
    sq = solar_query.SolarQuery(api_key=cfg.SOLAR_API_KEY, latitude=cfg.HOME_LATITUDE,
                                longitude=cfg.HOME_LONGITUDE, base_url=cfg.SOLAR_API_URL)
    wq = weather_query.WeatherQuery(api_key=cfg.WEATHER_API_KEY, latitude=cfg.HOME_LATITUDE,
                                    longitude=cfg.HOME_LONGITUDE, base_url=cfg.WEATHER_API_URL)
    return sq, wq


async def get_data() -> dict:
    """Retrieve data from queries."""
    _task_list = []
    sq, wq = _configure_objects()

    _task_list.append(asyncio.create_task(sq.get_data()))
    _task_list.append(asyncio.create_task(wq.get_data()))

    while _task_list:
        _, pending = await asyncio.wait(_task_list)
        _task_list[:] = pending

    cloud_cover, temperature = wq.parse_data()
    return {"cloud_cover": cloud_cover, "temperature": temperature, "radiation": sq.parse_data()}


if __name__ == '__main__':
    resp = asyncio.run(get_data())

    print(resp)
