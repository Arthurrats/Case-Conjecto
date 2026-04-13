# === CÓDIGO PARA A TRANSFORMAÇÃO DE DADOS ===

# Importa bibliotecas necessárias.
import pandas as pd
import os
import logging

# Função: transforma dados já extraídos.
def transformacao_dados(nome_arquivo):
    """Lê o dado bruto da pasta data/raw e faz transformações com métricas iniciais."""
    caminho_entrada = os.path.join("data", "raw", f"{nome_arquivo}.csv")
    caminho_saida = os.path.join("data", "processed", f"{nome_arquivo}_clean.csv")

    # Tratando erros.
    try:
        logging.info(f"--- INICIANDO A TRANSFORMAÇÃO: {nome_arquivo} ---")

        # Carregando o csv bruto.
        df = pd.read_csv(caminho_entrada)

        # Tratamento 1: tratando Datas.
        df['data'] = pd.to_datetime(df['data'], dayfirst=True)

        # Tratamento 2: tratando números (5,10 --> 5.10).
        if df['valor'].dtype == 'O':
            df['valor'] = df['valor'].str.replace(",", ".").astype(float)

        # Tratamento 3: tratando as duplicidades.
        df = df.dropna().drop_duplicates().sort_values('data')

        # Métrica 1: calculando a variação do percentual diário/mensal.
        df['variavao_percentual'] = df['valor'].pct_change() * 100

        # Métrica 2: calculando picos de volatilidade.
        df['pico_volatilidade'] = df['variavao_percentual'].apply(lambda x: True if abs(x) > 1.0 else False)

        # Tratando erro: garate que a pasta de destino exista.
        os.makedirs("data/processed", exist_ok=True)

        # Salva os dados limpos (Camada Silver)
        df.to_csv(caminho_saida, index=False)

        # Mensagem de sucesso após a execução correta.
        logging.info(f"Sucesso: o {nome_arquivo} foi salvo com sucesso em {caminho_saida}.")
        return True
    
    # Tratando exceções.
    except Exception as e:
        logging.error(f"Erro: falha no processo de transformação de {nome_arquivo}: {e}")
        return False