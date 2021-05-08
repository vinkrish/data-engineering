DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(255) PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    gender CHAR,
    level VARCHAR(16) NOT NULL);