# === CÓDIGO PARA A EXECUÇÃO DA NOSSA EXTRAÇÃO ===

# Importando bibliotecas necessárias.
from src.extract import extracao
import os

# Execução: executando a nossa extração.
def run_pipeline():
    print("--- INICIANDO PIPELINE DE DADOS ---\n")

    # Diciónario com as séries que iremos trabalhar.
    series = {
        10813 : "dolar_comercial",
        432 : "taxa_selic",
        433 : "inflacao"
    }

    # Percorrendo as séries no dicionário.
    for cod, nome in series.items():
        # Chama a função de extração
        sucesso = extracao(cod, nome)
        
        # Tratamento de erro para séries inexistentes.
        if sucesso:
            print(f"Sucesso: dados de {nome} coletados.")
        else:
            print(f"Erro: falha ao coletar {nome}. Verifique os logs.")

    print("\n--- EXTRAÇÃO CONCLUÍDA COM SUCESSO ---")

if __name__ == "__main__":
    run_pipeline()