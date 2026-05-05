from produtos_database import get_connection


class ProdutoRepository:
    def create(self, nome: str, descricao: str, preco: float):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO produtos (nome, descricao, preco)
            VALUES (?, ?, ?) """,
                       (nome, descricao, preco))

        conn.commit()
        ultimo_id = cursor.lastrowid
        conn.close()

        return ultimo_id

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, nome, descricao, preco FROM produtos where status = 1")
        rows = cursor.fetchall()

        conn.close()

        return rows

    def get_by_id(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, nome, descricao, preco, status FROM produtos WHERE id = ?", (
                id,)
        )
        row = cursor.fetchone()
        conn.close()

        return row

    def update(self, id: int, nome: str, descricao: str, preco: float, status: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE produtos
            SET nome = ?, descricao = ?, preco = ?, status = ?
            WHERE id = ? """,
                       (nome, descricao, preco, status, id)
                       )

        conn.commit()
        affected = cursor.rowcount
        conn.close()

        return affected

    def delete(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
        conn.commit()
        affected = cursor.rowcount
        conn.close()

        return affected
