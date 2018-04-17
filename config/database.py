import sqlite3

def open_cursor():
    conn = sqlite3.connect('simplefeedbot.sqlite')
    cursor = conn.cursor()
    return conn, cursor

def close_cursor(conn, cursor):
    cursor.close()
    conn.close()

def sync_db():
    conn, cursor = open_cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS feeds (id integer PRIMARY KEY, url TEXT NOT NULL);")
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY, userid INTEGER NOT NULL);")
    cursor.execute("CREATE TABLE IF NOT EXISTS links (id integer PRIMARY KEY, guid INTEGER NOT NULL, feed_id int NOT NULL, FOREIGN KEY (feed_id) REFERENCES feeds (id));")
    cursor.execute("CREATE TABLE IF NOT EXISTS userfeeds (id integer PRIMARY KEY, user_id INTEGER NOT NULL, feed_id INTEGER NOT NULL, FOREIGN KEY (user_id) REFERENCES users (id), FOREIGN KEY (feed_id) REFERENCES feeds (id));")
    close_cursor(conn, cursor)