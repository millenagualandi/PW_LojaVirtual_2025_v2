from typing import Optional
from data.forma_pagamento_model import FormaPagamento
from data.forma_pagamento_sql import *
from data.util import get_connection


def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA)
    conn.commit()
    conn.close()


def inserir(forma_pagamento: FormaPagamento):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(INSERIR, (
        forma_pagamento.nome, 
        forma_pagamento.desconto))
    conn.commit()
    conn.close()


def obter_todas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_TODOS)
    tuplas = cursor.fetchall()
    conn.close()
    return [FormaPagamento(
        id=tupla[0], 
        nome=tupla[1], 
        desconto=tupla[2])
        for tupla in tuplas]
