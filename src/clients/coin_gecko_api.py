from datetime import datetime

from pydantic import BaseModel
from requests import Session
from tenacity import retry, stop_after_attempt, wait_exponential


class MarketParams(BaseModel):
    vs_currency: str = "usd"
    order: str = "market_cap_desc"
    per_page: int = 10
    page: int = 1


class MarketResponse(BaseModel):
    id: str
    symbol: str
    name: str
    current_price: float
    market_cap: int
    total_volume: int
    last_updated: datetime


class CoinGeckoApi:
    """Class for work with CoinGecko API"""
    BASE_URL = "https://api.coingecko.com/api/v3/"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    @retry(
        stop=stop_after_attempt(7),
        wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    def fetch_daily_market_data(self, params: MarketParams) -> list[MarketResponse]:
        """
        This method requests supported coins with price,
        market cap, volume and market related data.
        """
        url = self.BASE_URL + "coins/markets"
        headers = {"x-cg-demo-api-key": self.api_key}
        data = []

        with Session() as session:
            session.headers.update(headers)
            response = session.get(url, params=params.model_dump())

            if response.status_code != 200:
                response.raise_for_status()

            data = response.json()

        return [MarketResponse.model_validate(item) for item in data]
