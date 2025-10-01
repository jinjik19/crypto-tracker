
from datetime import datetime

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from tenacity import RetryError

from clients.coin_gecko_api import CoinGeckoApi, MarketParams, MarketResponse
from config.settings import settings
from utils.logger import logger


def extract_data() -> list[MarketResponse]:
    """Function extract data from coingecko."""
    client = CoinGeckoApi(settings.api_key)

    try:
        logger.debug("Try to fetch daily market data")
        return client.fetch_daily_market_data(params=MarketParams()) # type: ignore
    except RetryError as e:
        logger.warning(f"Cannot fetch data: {e}")
        return []


def transform_data(data: list[MarketResponse]) -> pd.DataFrame:
    """Function transform and clean data."""
    df = pd.DataFrame([item.model_dump() for item in data])
    # df["updated_at"] = df["last_updated"].astype('int64') // 10**9
    df["fetch_date"] = datetime.now().date()
    # df.drop('last_updated', axis='columns', inplace=True)
    df.rename(columns={"id": "crypto_id", "last_updated": "updated_at"}, inplace=True)

    return df


def save_data(cleaned_data: pd.DataFrame) -> None:
    """Function save cleaned data to DB"""
    engine = create_engine(settings.db_url)

    with engine.begin() as conn:
        try:
            cleaned_data.to_sql(
                name="crypto_prices_daily", con=conn, if_exists="append", index=False
            )
        except IntegrityError:
            logger.warning("Data already saved into table.")


def main() -> None:
    """Function is main entrypoint."""
    logger.info("Start fetch data for top-10 cryptocurrency.")
    data = extract_data()

    if len(data) > 0:
        logger.info("Transforming fetched data...")
        cleaned_data = transform_data(data)
        logger.info("Saving cleaned data...")
        save_data(cleaned_data)
        logger.info("Cryptocurrency data saved!")




if __name__ == "__main__":
    main()
