from repositories.produto_repository import ProdutoRepository


class ProdutoService:
    def __init__(self):
        self.repository = ProdutoRepository()

    def criar_produto(self, nome: str, descricao: str, preco: float):
        if preco < 0:
            return "O preço não pode ser negativo!"
        return self.repository.create(nome, descricao, preco)

    def listar_produtos(self):
        produtos = self.repository.get_all()
        return [dict(produto) for produto in produtos]

    def buscar_produto_por_id(self, id: int):
        produto = self.repository.get_by_id(id)
        if not produto:
            return None

        return dict(produto)

    def atualizar_produto(self, id: int, nome: str, descricao: str, preco: float, status: int):
        if preco < 0:
            return "O preço não pode ser negativo!"
        return self.repository.update(id, nome, descricao, preco, status)

    def excluir_produto(self, id: int):
        produto = self.repository.get_by_id(id)
        if not produto:
            return None
        print(produto)

        if produto['status'] == 0:
            return self.repository.delete(id)

        return "produto ativo"
