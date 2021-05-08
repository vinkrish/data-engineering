import pandas as pd
from sql_queries import *
from airflow.providers.postgres.hooks.postgres import PostgresHook

def process_song_file(filepath):
    """
    Reads from song datasource and loads data into song and artist tables
    :param filepath: Source data location
    """
    
    postgres_hook = PostgresHook(postgres_conn_id='local_postgres', schema='postgres')
    conn = postgres_hook.get_conn()
    cur = conn.cursor()

    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0].tolist()
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)

    cur.close()
    conn.commit()
