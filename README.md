# Case Conjecto - Pipeline de Indicadores Econômicos 📈

Este projeto consiste em uma Pipeline de Dados automatizada que extrai, transforma e analisa indicadores econômicos cruciais *(Dólar, Selic e Inflação)* diretamente da API pública do Banco Central do Brasil *(SGS - Sistema Gerenciador de Séries Temporais)*.

O objetivo é fornecer uma visão clara e analitica da relação entre política monetária, câmbio e custo de vida no cenário de 2026.

## 🏗️ Estrutura do Projeto

A solução foi desenhada seguindo os princípios de modularização e separação de responsabilidades:

![Arquitetura da Pipeline](./pipeline_arquitetura.png)

### Estrutura de diretório

```text
CASE_CONJECTO/
├── data/                  # Armazenamento de dados (Persistência)
│   ├── insights/          # Gráficos (PNG) e relatórios de texto (TXT)
│   ├── processed/         # Dados limpos e transformados (Camada Silver)
│   └── raw/               # Dados brutos extraídos da API (Camada Bronze)
├── logs/                  # Registros de execução da pipeline
├── src/                   # Código fonte modularizado
│   ├── __init__.py
│   ├── extract.py         # Lógica de consumo da API do BCB
│   ├── transform.py       # Limpeza e cálculos estatísticos
│   └── analysis.py        # Geração de visualizações e insights
├── Dockerfile             # Configuração da imagem Docker
├── main.py                # Ponto de entrada (Orquestrador da Pipeline)
├── requeriments.txt       # Dependências do projeto
└── README.md              # Documentação principal
```

## 🚀 Como Executar

A pipeline foi totalmente "dockerizada" para garantir que rode em qualquer ambiente sem necessidade de instalar dependências localmente.

**1. Clonar o Repositório**

```
git clone [https://github.com/arthurrats/case_conjecto.git](https://github.com/seu-usuario/case_conjecto.git)
```
```
cd case_conjecto
```

**2. Pré-requisitos**

```text
Docker instalado e rodando.
```

**2. Construir a Imagem**

No terminal, dentro da pasta do projeto, execute:

```text
docker build -t case_conjecto .
```

**3. Rodar a Pipeline**

Para que os dados e gráficos gerados fiquem salvos na sua máquina, utilize o mapeamento de volumes:

```text
docker run -v $(pwd)/data:/app/data -v $(pwd)/logs:/app/logs case_conjecto
```

## 🛠️ Tecnologias Utilizadas

**Python 3.10**: Linguagem base.

**Pandas**: Manipulação e tratamento de dados.

**Requests**: Consumo de API REST.

**Matplotlib** & **Seaborn**: Geração de gráficos.

**Docker**: Conteinerização da aplicação.

## O que essa Pipeline entrega?

Ao final da execução, verifique a pasta *data/insights* para encontrar:

**Relatório Visual:** Comparativo entre a variação do Dólar e a taxa Selic.

**Relatório de Inflação**: Gráfico de barras com a evolução mensal do IPCA.

**Insights de Negócio**: Um sumário em texto com correlação estatística e volatilidade.
