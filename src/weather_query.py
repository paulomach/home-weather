"""Weather query."""
import requests

from query import Query


class WeatherQuery(Query):
    """Weather query class."""

    def __init__(self, api_key: str, latitude: str, longitude: str, base_url: str):
        """Initialize the class.

        Args:
            api_key (str): API key.
            lat (str): Latitude.
            long (str): Longitude.
            base_url (str): Base URL.
        """
        super().__init__(api_key, latitude, longitude, base_url)
        self.query_string = {
            "key": api_key,
            "q": f"{latitude},{longitude}",
            "aqi": "no",
        }

    async def get_data(self):
        """Get weather.

        Returns:
            dict: Weather.
        """
        try:
            response = requests.get(self.base_url, params=self.query_string)
        except TimeoutError:
            return None

        self.result = response.json()

    def parse_data(self):
        """Parse weather.

        Args:
            weather (dict): Weather.

        Returns: cloud, temp tuple.
        """
        current = self.result.get("current")

        return current['cloud'], current['temp_c']


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--api_key", type=str, required=True)
    parser.add_argument("--lat", type=str, default="-27.119")
    parser.add_argument("--long", type=str, default="-109.366")
    parser.add_argument("--base_url", type=str,
                        default="http://api.weatherapi.com/v1/current.json")

    args = parser.parse_args()

    wq = WeatherQuery(args.api_key, args.lat, args.long, args.base_url)
    wq.get_data()
    cc, temp = wq.parse_data()
    print(f"Cloud cover: {cc}")
    print(f"Temperature: {temp}")
