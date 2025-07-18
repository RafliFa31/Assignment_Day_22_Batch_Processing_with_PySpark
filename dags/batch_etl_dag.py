from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='batch_etl_pyspark',
    default_args=default_args,
    description='DAG untuk ETL harian dengan PySpark',
    schedule_interval='@daily',
    start_date=datetime(2025, 7, 17),
    catchup=False,
    tags=['batch', 'etl', 'pyspark'],
) as dag:

    run_etl = BashOperator(
        task_id='run_batch_etl',
        bash_command='spark-submit /opt/airflow/pyspark_scripts/batch_etl_day.py >> /opt/airflow/logs/etl_output.log 2>&1'
    )

    run_etl
