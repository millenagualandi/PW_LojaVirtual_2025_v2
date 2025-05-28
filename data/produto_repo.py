from data.produto_model import Produto
from data.produto_sql import *
from data.util import get_connection

def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA)
    conn.commit()
    conn.close()

def inserir(produto: Produto):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(INSERIR, (
        produto.nome, 
        produto.descricao, 
        produto.preco, 
        produto.quantidade))
    conn.commit()
    conn.close()

def obter_todos() -> list[Produto]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_TODOS)
    tuplas = cursor.fetchall()
    conn.close()
    produtos = [
        Produto(
            id=tupla[0], 
            nome=tupla[1], 
            descricao=tupla[2], 
            preco=tupla[3], 
            quantidade=tupla[4])
            for tupla in tuplas]
    return produtos