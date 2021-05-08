DROP TABLE IF EXISTS artists;

CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR(255) PRIMARY KEY, 
    name VARCHAR(255) NOT NULL, 
    location VARCHAR(255) NOT NULL, 
    latitude real NULL, 
    longitude real NULL);