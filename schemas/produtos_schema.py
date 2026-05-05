from pydantic import BaseModel


class ProdutoCreate(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    status: int
