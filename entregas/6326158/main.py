import mod_estoque


def main():
    itens = []

    itens.append(mod_estoque.cadastrar_item("Teclado", 10, 80.00))
    itens.append(mod_estoque.cadastrar_item("Mouse", 4, 50.00))
    itens.append(mod_estoque.cadastrar_item("Monitor", 2, 750.00))

    total = mod_estoque.calcular_valor_estoque(itens)

    minimo = 5
    itens_em_falta = mod_estoque.listar_itens_em_falta(itens, minimo)

    print(f"Valor total do estoque: R$ {total:.2f}")
    print("Itens em falta:")

    for item in itens_em_falta:
        print(item)


if __name__ == "__main__":
    main()