import os
import glob
import datetime
import logging
import psycopg2

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
# from airflow.operators.postgres_operator import PostgresOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

from log_process import process_log_file
from song_process import process_song_file

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['vinaykrishna1989@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
}

dag = DAG(
    'audio_player',
    default_args=default_args,
    start_date=datetime.datetime.now(),
    schedule_interval=None
)

# create_tables_task = PythonOperator(
#     task_id='create_tables',
#     dag=dag,
#     postgres_conn_id='local_postgres',
#     database='test_db',
#     sql='create_tables.sql'
# )

create_artists_table = PostgresOperator(
    task_id="create_artists_table",
    postgres_conn_id="local_postgres",
    #database='test_db',
    sql="sql/artists_schema.sql",
    dag=dag
)

create_songplays_table = PostgresOperator(
    task_id="create_songplays_table",
    postgres_conn_id="local_postgres",
    #database='test_db',
    sql="sql/songplays_schema.sql",
    dag=dag
)

create_songs_table = PostgresOperator(
    task_id="create_songs_table",
    postgres_conn_id="local_postgres",
    #database='test_db',
    sql="sql/songs_schema.sql",
    dag=dag
)

create_time_table = PostgresOperator(
    task_id="create_time_table",
    postgres_conn_id="local_postgres",
    #database='test_db',
    sql="sql/time_schema.sql",
    dag=dag
)

create_users_table = PostgresOperator(
    task_id="create_users_table",
    postgres_conn_id="local_postgres",
    #database='test_db',
    sql="sql/users_schema.sql",
    dag=dag
)    

def process_data(*args, **kwargs):
    """
    Iterates over data source and applies a function to each data item
    """

    filepath = kwargs["filepath"]
    func = kwargs["func"]
    
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(datafile)
        print('{}/{} files processed.'.format(i, num_files))

song_folder = f"{os.environ.get('AIRFLOW_HOME')}/data/song_data"
process_song_file_task = PythonOperator(
    task_id="process_song_file",
    python_callable=process_data,
    op_kwargs={'filepath': '/Users/vinkrish/airflow/data/song_data', 'func': process_song_file},
    dag=dag
)

log_folder = f"{os.environ.get('AIRFLOW_HOME')}/data/log_data"
process_log_file_task = PythonOperator(
    task_id="process_log_file",
    python_callable=process_data,
    op_kwargs={'filepath': '/Users/vinkrish/airflow/data/log_data', 'func': process_log_file},
    dag=dag
)

create_artists_table >> create_songplays_table >> create_songs_table >> create_time_table >> create_users_table >> \
    process_song_file_task >> process_log_file_task