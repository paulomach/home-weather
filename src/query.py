"""Base query data class."""
from abc import ABC, abstractmethod


class Query(ABC):
    """Base query data class."""

    def __init__(self, api_key: str, latitude: str, longitude: str, base_url: str):
        """Initialize the class.

        Args:
            api_key (str): API key.
            latitude (str): Latitude.
            longitude (str): Longitude.
            base_url (str): Base URL.
        """
        self.result = None
        self.base_url = base_url
        self.query_string = {
            "key": api_key,
            "q": f"{latitude},{longitude}",
            "aqi": "no",
        }

    @abstractmethod
    async def get_data(self):
        """Get data from API."""
        pass

    @abstractmethod
    def parse_data(self):
        """Parse data from API."""
        pass
