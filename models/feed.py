from config import database

def get(url):
    conn, cursor = database.open_cursor()
    cursor.execute("SELECT * FROM feeds WHERE url = ?", (url,))
    dados = cursor.fetchone()
    database.close_cursor(conn, cursor)
    try:
        return dados[0]
    except Exception:
        return False

def get_all():
    conn, cursor = database.open_cursor()
    cursor.execute("SELECT * FROM feeds")
    return cursor.fetchall()

def add(url):
    feed_id = get(url)
    if(not feed_id):
        conn, cursor = database.open_cursor()
        cursor.execute("INSERT INTO feeds VALUES (?, ?)", (None, url))
        conn.commit()
        feed_id = cursor.lastrowid
        database.close_cursor(conn, cursor)
    return feed_id