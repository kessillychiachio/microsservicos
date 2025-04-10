import sqlite3

def criar_banco():
    conn = sqlite3.connect("catalogo.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS oleos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            beneficios TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
