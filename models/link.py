from config import database
from models import feed
from models import link

def get(guid, feed_id):
    conn, cursor = database.open_cursor()
    cursor.execute("SELECT * FROM links WHERE guid = ? AND feed_id = ?", (guid, feed_id))
    dados = cursor.fetchone()
    database.close_cursor(conn, cursor)
    try:
        return dados[0]
    except Exception:
        return False

def add(guid, feed_id):
    link_id = link.get(guid, feed_id)
    if(not link_id):
        conn, cursor = database.open_cursor()
        cursor.execute("INSERT INTO links VALUES (?, ?, ?)", (None, guid, feed_id))
        conn.commit()
        link_id = cursor.lastrowid
        database.close_cursor(conn, cursor)
    return link_id

def add_bkp(guid, url):
    feed_id = feed.get(url)
    link_id = link.get(guid, feed_id)
    if(not link_id):
        conn, cursor = database.open_cursor()
        cursor.execute("INSERT INTO links VALUES (?, ?, ?)", (None, guid, feed_id))
        conn.commit()
        link_id = cursor.lastrowid
        database.close_cursor(conn, cursor)
    return link_id