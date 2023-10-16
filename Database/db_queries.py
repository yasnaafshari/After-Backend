
CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS users ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT,
    password TEXT, 
    email TEXT UNIQUE NOT NULL, 
    note TEXT, 
    sendDate TIMESTAMP, 
    recipients LIST)"""

INSERT_USER_QUERY = """
INSERT INTO users (email, password) VALUES (?, ?);
"""

SELECT_ALL_USERS_QUERY = """
SELECT * FROM users;
"""

SELECT_USER_BY_EMAIL_QUERY = """
SELECT * FROM users WHERE email = ?;
"""
