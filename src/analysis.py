# === CÓDIGO PARA A APRESENTAÇÃO DE DADOS ===

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 
import seaborn as sns
import os

# Função: gera análises dos dados.
def analise_dado():
    # Carregando os dados processados.
    try:
        df_dolar = pd.read_csv("data/processed/dolar_comercial_clean.csv")
        df_selic = pd.read_csv("data/processed/taxa_selic_clean.csv")
        df_inflacao = pd.read_csv("data/processed/inflacao_clean.csv")

        # CONVERSÃO: garante o entendimento das datas.
        df_dolar['data'] = pd.to_datetime(df_dolar['data'])
        df_selic['data'] = pd.to_datetime(df_selic['data'])
        df_inflacao['data'] = pd.to_datetime(df_inflacao['data'])

        # Tratando erro: garante que a pasta de destino exista.
        os.makedirs("data/insights", exist_ok=True)
        sns.set_theme(style="whitegrid")

        # Gráfico 1: DÓLAR VS SELIC.
        fig, ax = plt.subplots(figsize=(12, 6))
        
        ax.plot(df_dolar['data'], df_dolar['valor'], label='Dólar (R$)', color='blue', linewidth=2)
        ax.plot(df_selic['data'], df_selic['valor'], label='Selic (%)', color='green', linestyle='--')

        # Alteração de datas: põe datas em momentos de pico
        ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2)) 
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))

        plt.title("Relação: Dólar vs Selic - Cenário 2026", fontsize=15)
        plt.xlabel('Período (Dia/Mês)')
        plt.ylabel('Valores')
        plt.legend()
        plt.xticks(rotation=0)

        # Salvando o gráfico de linhas.
        plt.tight_layout()
        plt.savefig("data/insights/relatorio_visual.png")
        plt.close()

        # Gráfico 2: inflação geral.
        plt.figure(figsize=(12, 6))
        
        # Exibir datas como 'Mês/Ano'.
        df_inflacao['mes_formatado'] = df_inflacao['data'].dt.strftime('%b/%y')
        
        sns.barplot(data=df_inflacao, x='mes_formatado', y='valor', color='red')
        plt.title("Variação Mensal: Inflação (IPCA) - 2026", fontsize=15)
        plt.xlabel('Mês')
        plt.ylabel('Variação (%)')

        # Salvando o gráfico de barras.
        plt.tight_layout()
        plt.savefig("data/insights/relatorio_inflacao.png")
        plt.close()

        # Confirmação dos arquivos salvos.
        print("Gráfico 'relatorio_visual.png' salvo em 'data/insights'.")
        print("Gráfico 'relatorio_inflacao.png' salvo em 'data/insights'.")

        # Cálculos para o relatório.
        ligacao = df_dolar['valor'].corr(df_selic['valor'])
        inflacao_total = df_inflacao['valor'].sum()

        # Variável que armazena o caminho.
        caminho = "data/insights/insights_negocio.txt"

        with open(caminho, 'w') as arquivo:
            arquivo.write("--- RELATÓRIO DE INSIGHTS ECONÔMICOS EM 2026 ---\n\n")
            arquivo.write(f"I. Correlação Dólar/selic: {ligacao:.2f}\n")
            arquivo.write("OBS.: Valores próximos de 1 indicam que a Selic subiu para acompanhar o Dólar.\n\n")
            
            arquivo.write("II. Volatilidade:\n")
            arquivo.write(f"O pico de variação do Dólar no período foi de {df_dolar['variavao_percentual'].max():.2f}%.\n\n")
            
            arquivo.write("III. Inflação Acumulada:\n")
            arquivo.write(f"A soma da variação do IPCA no período analisado foi de {inflacao_total:.2f}%.\n")

        print("Arquivo 'insights_negocio.txt' gerado com sucesso.")
        return True
    
    except Exception as e:
        print(f"Erro: falha na análise: {e}")
        return False