DROP TABLE IF EXISTS songplays;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS time;

CREATE TABLE IF NOT EXISTS songplays
(
songplay_id SERIAL,
start_time DATE,
user_id VARCHAR(255) NOT NULL,
level VARCHAR(16),
song_id VARCHAR(255),
artist_id VARCHAR(255),
session_id INTEGER,
location VARCHAR(255),
user_agent VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS users 
(
user_id VARCHAR(255) PRIMARY KEY,
first_name VARCHAR(255),
last_name VARCHAR(255),
gender CHAR,
level VARCHAR(16) NOT NULL
);

CREATE TABLE IF NOT EXISTS songs 
(
song_id VARCHAR(255) PRIMARY KEY,
title VARCHAR(255) NOT NULL,
artist_id VARCHAR(255) NOT NULL,
year INT NULL,
duration FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS artists 
(
artist_id VARCHAR(255) PRIMARY KEY, 
name VARCHAR(255) NOT NULL, 
location VARCHAR(255) NOT NULL, 
latitude real NULL, 
longitude real NULL
);

CREATE TABLE IF NOT EXISTS time
(
start_time TIME,
hour INT NULL,
day INT NULL,
week INT NULL,
month INT NULL,
year INT NULL,
weekday INT NULL
);
