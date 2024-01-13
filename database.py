import sqlite3 as sql
 
database_name = 'film_bot.db'


async def create_tables(db):
    con = sql.connect(database_name)
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS user(
                user_id INTEGER,
                username VARCHAR(100)
    )""")


    cur.execute("""CREATE TABLE IF NOT EXISTS film(
            film_code INTEGER,
            film_name VARCHAR(100),
            film_id TEXT
    )""")

async def create_user(user_id,username):
    con = sql.connect(database_name)
    cur = con.cursor()


    if cur.execute("SELECT * FROM user WHERE user_id = ?", (user_id,)).fetchone():
        cur.execute("INSTER INTO user VALUES (?, ?)", (user_id,username))
        con.commit()

async def create_film(film_code, film_name, film_id):
    con = sql.connect(database_name)
    cur = con.cursor()
    cur.execute("INSERT INTO film VALUES (?, ?, ?)", (film_code, film_name, film_id))
    con.commit()

async def get_film(code):
    con = sql.connect(database_name)
    cur = con.cursor()

    data = cur.execute("SELECT * FROM film WHERE film_code = ?",(code,)).fetchone()
    return data