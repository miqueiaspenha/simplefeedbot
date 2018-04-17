from config import database

def get(userid):
    conn, cursor = database.open_cursor()
    cursor.execute("SELECT * FROM users WHERE userid = ?", (userid,))
    dados = cursor.fetchone()
    database.close_cursor(conn, cursor)
    try:
        return dados[0]
    except Exception:
        return False

def get_all():
    conn, cursor = database.open_cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def add(userid):
    user_id = get(userid)
    if(not user_id):
        conn, cursor = database.open_cursor()
        cursor.execute("INSERT INTO users VALUES (?, ?)", (None, userid))
        conn.commit()
        user_id = cursor.lastrowid
        database.close_cursor(conn, cursor)
    return user_id