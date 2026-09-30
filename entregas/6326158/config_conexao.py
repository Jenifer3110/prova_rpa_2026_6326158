def main():
    ENDPOINT_URL = "https://api.exemplo.com"
    PORTA = 443
    TAXA_AMOSTRAGEM = 2.5
    USA_HTTPS = True

    parametros = {
        "ENDPOINT_URL": ENDPOINT_URL,
        "PORTA": PORTA,
        "TAXA_AMOSTRAGEM": TAXA_AMOSTRAGEM,
        "USA_HTTPS": USA_HTTPS
    }

    for nome, valor in parametros.items():
        print(f"{nome}: {valor} - tipo: {type(valor)}")


if __name__ == "__main__":
    main()