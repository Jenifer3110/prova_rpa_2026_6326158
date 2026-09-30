leituras = [36.5, 41.2, 38.0, 105.0, 37.4, -999.0, 39.1, 40.0]


def monitorar(lista):
    soma = 0.0
    quantidade = 0

    for leitura in lista:
        if leitura > 80.0:
            print(f"[DESCARTE] Leitura de {leitura}°C fora da faixa: ignorada.")
            continue

        if leitura == -999.0:
            print(f"[FALHA] Sensor corrompido ({leitura}). Interrompendo monitoramento...")
            break

        print(f"[OK] Leitura de {leitura}°C registrada.")
        soma += leitura
        quantidade += 1

    if quantidade > 0:
        media = soma / quantidade
        print(f"Quantidade de leituras válidas: {quantidade}")
        print(f"Média: {media:.2f}°C")
    else:
        print("Nenhuma leitura válida.")


if __name__ == "__main__":
    monitorar(leituras)