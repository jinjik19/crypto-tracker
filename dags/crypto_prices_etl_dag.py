
from datetime import datetime

from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.sdk import Variable, dag, task


@dag(
    dag_id="crypto_prices_etl_dag",
    schedule="30 1 * * *",
    start_date=datetime(2025, 10, 9),
    catchup=True,
    tags=["crypto_tracker", "etl"],
)
def crypto_etl_process() -> None:
    @task(task_id="get_config")
    def get_config():
        api_key = Variable.get("api_key")
        db_uri = PostgresHook(postgres_conn_id="dw_conn").get_uri()

        return {"api_key": api_key, "db_uri": db_uri}

    @task.virtualenv(
        task_id="run_etl",
        requirements="dependencies/requirements.txt",
        system_site_packages=False,
    )
    def run_crypto_etl(config: dict) -> None:
        import sys

        sys.path.insert(0, "/opt/airflow/src")

        from etl import run_etl

        api_key = config["api_key"]
        db_uri = config["db_uri"]

        run_etl(api_key, db_uri)

    config = get_config()
    run_crypto_etl(config)


crypto_etl_process()
