-- drop songplays table
DROP TABLE IF EXISTS songplays;

-- create songplays table
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL,
    start_time DATE,
    user_id VARCHAR(255) NOT NULL,
    level VARCHAR(16),
    song_id VARCHAR(255),
    artist_id VARCHAR(255),
    session_id INTEGER,
    location VARCHAR(255),
    user_agent VARCHAR(255));