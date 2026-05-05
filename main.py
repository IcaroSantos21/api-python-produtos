from fastapi import FastAPI
from produtos_database import create_table
from controllers.produto_controller import router as produto_router

app = FastAPI()

create_table()

app.include_router(produto_router)
