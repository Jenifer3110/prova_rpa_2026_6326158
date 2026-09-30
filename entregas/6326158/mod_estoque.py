def cadastrar_item(nome: str, quantidade: int, preco_unitario: float) -> dict:
    return {
        "nome": nome,
        "quantidade": quantidade,
        "preco_unitario": preco_unitario
    }


def calcular_valor_estoque(itens: list) -> float:
    total = 0.0

    for item in itens:
        total += item["quantidade"] * item["preco_unitario"]

    return total


def listar_itens_em_falta(itens: list, minimo: int) -> list:
    itens_em_falta = []

    for item in itens:
        if item["quantidade"] < minimo:
            itens_em_falta.append(item)

    return itens_em_falta