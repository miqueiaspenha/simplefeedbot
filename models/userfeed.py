from config import database

def get(user_id, feed_id):
    conn, cursor = database.open_cursor()
    cursor.execute("SELECT * FROM userfeeds WHERE user_id = ? AND feed_id = ?", (user_id, feed_id))
    dados = cursor.fetchone()
    database.close_cursor(conn, cursor)
    try:
        return dados[0]
    except Exception:
        return False

def get_by_user(user_id):
    conn, cursor = database.open_cursor()
    cursor.execute("SELECT feed_id FROM userfeeds WHERE user_id = ?", (user_id,))
    dados = cursor.fetchall()
    database.close_cursor(conn, cursor)
    return dados

def get_users_by_feed(feed_id):
    conn, cursor = database.open_cursor()
    cursor.execute("SELECT user_id FROM userfeeds WHERE feed_id = ?", (feed_id,))
    dados = cursor.fetchall()
    database.close_cursor(conn, cursor)
    return dados

def add(user_id, feed_id):
    userfeed_id = get(user_id, feed_id)
    if(not userfeed_id):
        conn, cursor = database.open_cursor()
        cursor.execute("INSERT INTO userfeeds VALUES (?, ?, ?)", (None, user_id, feed_id))
        userfeed_id = cursor.lastrowid
        conn.commit()
        database.close_cursor(conn, cursor)
        return userfeed_id
    return False