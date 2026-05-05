class ProdutoModel:
    def __init__(self, id: int, nome: str, descricao: str, preco: float, status: int):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.status = status
