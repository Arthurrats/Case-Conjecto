# === CÓDIGO PARA A EXECUÇÃO DA NOSSA EXTRAÇÃO ===

# Importando bibliotecas necessárias.
from src.extract import extracao_dados
from src.transform import transformacao_dados
from src.analysis import analise_dado
import os

# Execução: executando a nossa extração.
def run_pipeline():
    # Dicionário com as séries.
    series = {
        10813 : "dolar_comercial",
        11 : "taxa_selic",
        433 : "inflacao"
    }

    # ETAPA 1: EXTRAÇÃO (Camada Raw)
    print("\nPASSO 1: EXTRAÇÃO DE DADOS (API BCB - SGS)")

    for cod, nome in series.items():
        # Chama a função de extração.
        sucesso_ext = extracao_dados(cod, nome)
        
        if sucesso_ext:
            print(f"Dados de {nome.upper()} coletados.")
        else:
            print(f"Falha ao coletar {nome.upper()}. Verifique os logs.")

    print(">>> EXTRAÇÃO CONCLUÍDA <<<\n")

    # ETAPA 2: TRANSFORMAÇÃO (Camada Silver)
    print("PASSO 2: TRANSFORMAÇÃO E LIMPEZA")

    for nome in series.values():
        # Chama a função de transformação.
        sucesso_trans = transformacao_dados(nome)
        
        if sucesso_trans:
            print(f"Dados de {nome.upper()} transformados.")
        else:
            print(f"Falha ao transformar {nome.upper()}.")
    
    print(">>> TRANSFORMAÇÃO CONCLUÍDA <<<\n")

if __name__ == "__main__":
    run_pipeline()


# ETAPA 3: GERAÇÃO DE INSIGHTS.
print("PASSO 3: GERAÇÃO DE INSIGTHS")
analise_dado()

print("\n*** PIPELINE CONCLUÍDA COM SUCESSO ***\n")