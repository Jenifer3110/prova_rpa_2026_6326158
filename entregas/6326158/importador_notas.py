# =============================================================================
# Questao 4 - Importacao de Notas Fiscais com pandas (Aula 04)

import logging
import pandas as pd


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("importacao.log"),
        logging.StreamHandler()
    ]
)


def importar_notas(caminho: str) -> float:
    """Importa notas de um CSV e retorna o total faturado."""

    try:
        dados = pd.read_csv(caminho)

        for _, nota in dados.iterrows():
            logging.info(
                f"Nota: {nota['nota']} - Cliente: {nota['cliente']} - Valor: {nota['valor']}"
            )

        total = dados["valor"].sum()
        logging.info(f"Total faturado: {total}")

        return float(total)

    except FileNotFoundError:
        logging.error(f"Arquivo não encontrado: {caminho}")
        return 0.0

    except pd.errors.EmptyDataError:
        logging.error(f"Arquivo CSV vazio: {caminho}")
        return 0.0

    finally:
        logging.info(f"Finalizada tentativa de importação: {caminho}")


if __name__ == "__main__":
    importar_notas("notas.csv")
    importar_notas("arquivo_inexistente.csv")