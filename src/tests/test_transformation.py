from datetime import date

import pandas as pd
import pytest
from pydantic import ValidationError

from clients.coin_gecko_api import MarketResponse
from main import transform_data


def test_transform_data_success():
    sample_api_data = [
        {
            "id": "bitcoin",
            "symbol": "btc",
            "name": "Bitcoin",
            "current_price": 65000.50,
            "market_cap": 1200000000000,
            "total_volume": 50000000000,
            "last_updated": "2025-10-01T10:00:00.123Z",
        }
    ]
    pydantic_objects = [MarketResponse.model_validate(item) for item in sample_api_data]

    result_df = transform_data(pydantic_objects)

    assert isinstance(result_df, pd.DataFrame)
    assert len(result_df) == 1
    assert "crypto_id" in result_df.columns
    assert "updated_at" in result_df.columns
    assert result_df.iloc[0]["crypto_id"] == "bitcoin"
    assert result_df.iloc[0]["current_price"] == 65000.50
    assert result_df.iloc[0]["fetch_date"] == date.today()


def test_pydantic_validation_fails_on_missing_data():
    malformed_api_data = [
        {
            "symbol": "btc",
            "name": "Bitcoin",
            "current_price": 65000.50,
            "market_cap": 1200000000000,
            "total_volume": 50000000000,
            "last_updated": "2025-10-01T10:00:00.123Z",
        }
    ]

    with pytest.raises(ValidationError):
        [MarketResponse.model_validate(item) for item in malformed_api_data]
