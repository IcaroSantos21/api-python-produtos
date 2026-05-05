from fastapi import APIRouter
from schemas.produtos_schema import ProdutoCreate
from services.produto_service import ProdutoService

router = APIRouter()
service = ProdutoService()


@router.post("/produtos")
def criar_produto(produto: ProdutoCreate):
    ultimo_id = service.criar_produto(
        produto.nome, produto.descricao, produto.preco)
    if isinstance(ultimo_id, str):
        return {
            "message": ultimo_id,
            "status_code": 401,
            "content": None
        }

    return {
        "message": f"Produto {ultimo_id} criado com sucesso!",
        "status_code": 201,
        "content": ultimo_id
    }


@router.get("/produtos")
def listar_produtos():
    produtos = service.listar_produtos()
    return {
        "message": "OK",
        "status_code": 200,
        "content": produtos
    }


@router.get("/produtos/{id}")
def buscar(product_id: int):
    produto = service.buscar_produto_por_id(product_id)
    if not produto:
        return {
            "message": "Produto não encontrado",
            "status_code": 404,
            "content": None
        }
    return {
        "message": "OK",
        "status_code": 200,
        "content": produto
    }


@router.put("/produtos/{id}")
def atualizar(product_id: int, produto: ProdutoCreate):
    linhas_afetadas = service.atualizar_produto(
        product_id, produto.nome, produto.descricao, produto.preco, produto.status
    )

    if linhas_afetadas == 0:
        return {
            "message": "Produto não encontrado",
            "status_code": 404,
            "content": None
        }

    return {
        "message": "Produto atualizado com sucesso!",
        "status_code": 200,
        "content": None
    }


@router.delete("/produtos/{id}")
def deletar(product_id: int):
    linhas_afetadas = service.excluir_produto(product_id)

    if isinstance(linhas_afetadas, str):
        return {
            "message": linhas_afetadas,
            "status_code": 401,
            "content": None
        }

    if linhas_afetadas == 0:
        return {
            "message": "Produto não encontrado",
            "status_code": 404,
            "content": None
        }

    return {
        "message": "Produto excluído com sucesso!",
        "status_code": 200,
        "content": None
    }
