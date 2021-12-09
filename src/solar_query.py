"""Query solcast radiation API."""
import requests

from query import Query


class SolarQuery(Query):
    """Solcast API layer."""

    def __init__(self, base_url: str, latitude: str, longitude: str, api_key: str):
        """Initialize the class.

        Args:
            base_url (str): SolCast API URL.
            latitude (str): The latitude.
            longitude (str): The longitude.
            api_key (str): SolCast API key.
        """
        super().__init__(api_key, latitude, longitude, base_url)
        self.query_string = {"latitude": latitude,
                             "longitude": longitude, "hours": "7", "format": "json"}
        self.headers = {
            "Authorization": f"Bearer {api_key}"
        }

    async def get_data(self):
        """Get data from the API."""
        response = requests.get(
            self.base_url, params=self.query_string, headers=self.headers)
        self.result = response.json()

    def parse_data(self):
        """Extract data from the API response.

        Args: data (dict): The API response.
        """
        estimated_actuals = self.result.get("estimated_actuals")

        ghi = []

        if estimated_actuals.__len__() > 0:
            for item in estimated_actuals:
                ghi.append(item["ghi"])
            return int(sum(ghi)/len(ghi))
        else:
            return 0


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser('Test the SolarQuery class.')
    parser.add_argument(
        '--base_url', type=str,
        default="https://api.solcast.com.au/world_radiation/estimated_actuals")
    parser.add_argument('--latitude', type=str, default="-50.604167")
    parser.add_argument('--longitude', type=str, default="165.973")
    parser.add_argument('--api_key', type=str, required=True,
                        help="API key for solcast.com.au")

    args = parser.parse_args()
    sq = SolarQuery(base_url=args.base_url, latitude=args.latitude,
                    longitude=args.longitude, api_key=args.api_key)

    response = sq.get_data()
    value = sq.parse_data()

    print(value)
