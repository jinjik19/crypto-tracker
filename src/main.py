
import pandas as pd
from tenacity import RetryError

from clients.coin_gecko_api import CoinGeckoApi, MarketParams, MarketResponse
from config.settings import settings


def extract_data() -> list[MarketResponse]:
    """Function extract data from coingecko."""
    client = CoinGeckoApi(settings.api_key)

    try:
        return client.fetch_daily_market_data(params=MarketParams())
    except RetryError:
        return []


def transform_data(data: list[MarketResponse]) -> pd.DataFrame:
    """Function transform and clean data."""
    df = pd.DataFrame([item.model_dump() for item in data])
    # 1. format last_updated to timestamp
    # 2. add new field fetch_date

    return df


def main() -> None:
    """Function is main entrypoint."""
    data = extract_data()

    if len(data) > 0:
        cleaned_data = transform_data(data)



if __name__ == "__main__":
    main()
