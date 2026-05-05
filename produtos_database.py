import sqlite3

DB_NAME = 'produtos.db'


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row

    return conn


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            preco FLOAT NOT NULL,
            status INTEGER NOT NULL DEFAULT 1)
        """
                   )

    conn.commit()
    conn.close()
