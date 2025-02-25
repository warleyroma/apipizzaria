import mysql.connector
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Configuração do banco de dados
DB_CONFIG = {
    "host": "3.83.68.65",  # IP do MySQL na AWS
    "port": 3306,
    "user": "warley",
    "password": "Denisia@23",
    "database": "pizzaria"
}

# Inicializar a API
app = FastAPI()

# Modelo para Cliente
class Cliente(BaseModel):
    nome: str
    telefone: str

# Modelo para Produto
class Produto(BaseModel):
    nome: str
    descricao: str
    preco: float

# Modelo para Pedido
class Pedido(BaseModel):
    cliente_id: int
    status: str
    total: float

# Rota para criar um cliente
@app.post("/clientes/")
def criar_cliente(cliente: Cliente):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO clientes (nome, telefone) VALUES (%s, %s)", (cliente.nome, cliente.telefone))
        conn.commit()
        return {"message": "Cliente criado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Rota para listar clientes
@app.get("/clientes/")
def listar_clientes():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return clientes

# Rota para criar um produto
@app.post("/produtos/")
def criar_produto(produto: Produto):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO produtos (nome, descricao, preco) VALUES (%s, %s, %s)",
                       (produto.nome, produto.descricao, produto.preco))
        conn.commit()
        return {"message": "Produto criado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Rota para listar produtos
@app.get("/produtos/")
def listar_produtos():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()
    return produtos

# Rota para criar um pedido
@app.post("/pedidos/")
def criar_pedido(pedido: Pedido):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO pedidos (cliente_id, status, total) VALUES (%s, %s, %s)",
                       (pedido.cliente_id, pedido.status, pedido.total))
        conn.commit()
        return {"message": "Pedido criado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Rota para listar pedidos
@app.get("/pedidos/")
def listar_pedidos():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pedidos")
    pedidos = cursor.fetchall()
    cursor.close()
    conn.close()
    return pedidos

# Comando para rodar no Google Colab
# !uvicorn app:app --host 0.0.0.0 --port 8000 --reload



