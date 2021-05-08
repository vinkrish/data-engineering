DROP TABLE IF EXISTS songs;

CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR(255) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    artist_id VARCHAR(255) NOT NULL,
    year INT NULL,
    duration FLOAT NOT NULL);