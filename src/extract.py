# === CÓDIGO PARA A EXTRAÇÃO DE DADOS VIA API: BCB - (SGS) ===

# Importa bibliotecas necessárias.
import requests
import pandas as pd
import os
import logging
from datetime import datetime, timedelta

# Handle de arquivo: salva um arquivo de INFO na pasta 'logs'.
logging.basicConfig(
    filename='logs/pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Função: extrai dados do bcb (Banco Central).
def extracao(codigo, nome_arquivo):
    """Consome a API do Banco Central (SGS) com tratamentos de erros."""

    # Definindo o período: 01/01/2026 até 3 dias atrás (D-3).
    data_inicio = "01/01/2026"
    data_fim = (datetime.now() - timedelta(days=3)).strftime('%d/%m/%Y') 

    # URL da API.
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json&dataInicial={data_inicio}&dataFinal={data_fim}"

    # Tratando erros.
    try: 
        logging.info(f"Iniciando a extração da série {codigo} - ({nome_arquivo})")

        # Limita a requisição em 15 segundos.
        response = requests.get(url, timeout=30)

        # Verifica se o retorno da API é 200.
        response.raise_for_status()

        # Convertendo os dados para o formato (.json).
        dados = response.json()

        # Tratando erro de dados nulos.
        if not dados:
            logging.warning(f"A série {codigo} retornou vazia.")
            return False
        
        # Converte os dados em DataFrame e envia para a pasta 'data/raw'
        df = pd.DataFrame(dados)
        caminho_final = os.path.join("data", "raw", f"{nome_arquivo}.csv")
        df.to_csv(caminho_final, index=False)

        # Mensagem de sucesso.
        logging.info(f"Sucesso: {len(df)} registros salvos em {caminho_final}.")
        return True
    
    # Tratando erros de séries (dados).
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro de conexão na série {codigo}: {e}.")
        return False
    except Exception as e:
        logging.error(f"Erro inesperado na série {codigo}: {e}.")
        return False