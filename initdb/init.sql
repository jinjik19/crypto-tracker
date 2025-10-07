CREATE DATABASE metabase_db;

CREATE TABLE IF NOT EXISTS crypto_prices_daily (
    fetch_date    DATE,
    crypto_id     VARCHAR(50),
    symbol        VARCHAR(50),
    name          VARCHAR(100),
    current_price NUMERIC(20, 10),
    market_cap    BIGINT,
    total_volume  BIGINT,
    updated_at    TIMESTAMP WITH TIME ZONE,
    PRIMARY KEY (fetch_date, crypto_id)
);