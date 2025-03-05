from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr
from enum import Enum
from db_connection import db  # Importando a conexão com Firestore

app = FastAPI()

# Criando Enum para status do pedido
class StatusPedido(str, Enum):
    PENDENTE = "pendente"
    FINALIZADO = "finalizado"
    CANCELADO = "cancelado"

# Modelos Pydantic
class ClienteCreate(BaseModel):
    nome: str
    telefone: constr(regex=r"^\d{10,11}$")  # Apenas números com 10-11 dígitos

class ProdutoCreate(BaseModel):
    nome: str
    descricao: str
    preco: float

class PedidoCreate(BaseModel):
    cliente_id: str  # Firestore usa strings como IDs
    status: StatusPedido
    total: float

# Rota para criar cliente
@app.post("/clientes/")
def criar_cliente(cliente: ClienteCreate):
    doc_ref = db.collection("clientes").add(cliente.dict())
    return {"message": "Cliente criado com sucesso!", "id": doc_ref[1].id}

# Rota para listar clientes
@app.get("/clientes/")
def listar_clientes():
    clientes_ref = db.collection("clientes").stream()
    clientes = [{**doc.to_dict(), "id": doc.id} for doc in clientes_ref]
    return clientes

# Rota para criar produto
@app.post("/produtos/")
def criar_produto(produto: ProdutoCreate):
    doc_ref = db.collection("produtos").add(produto.dict())
    return {"message": "Produto criado com sucesso!", "id": doc_ref[1].id}

# Rota para listar produtos
@app.get("/produtos/")
def listar_produtos():
    produtos_ref = db.collection("produtos").stream()
    produtos = [{**doc.to_dict(), "id": doc.id} for doc in produtos_ref]
    return produtos

# Rota para criar pedido
@app.post("/pedidos/")
def criar_pedido(pedido: PedidoCreate):
    doc_ref = db.collection("pedidos").add(pedido.dict())
    return {"message": "Pedido criado com sucesso!", "id": doc_ref[1].id}

# Rota para listar pedidos
@app.get("/pedidos/")
def listar_pedidos():
    pedidos_ref = db.collection("pedidos").stream()
    pedidos = [{**doc.to_dict(), "id": doc.id} for doc in pedidos_ref]
    return pedidos

@app.get("/")
def read_root():
    return {"message": "API está rodando!"}
