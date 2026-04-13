# Imagem do python
FROM python:3.10-slim
# Diretório dentro do Docker
WORKDIR /app
# Copia o arquivo de depenência
COPY requeriments.txt .
# Instala as dependências
RUN pip install --no-cache-dir -r requeriments.txt
# Copia todo o conteúdo do projeto para o container
COPY . .
# Cria as pastas necessárias
RUN mkdir -p data/raw data/processed logs
# Comando para rodar a Pipieline
CMD ["python", "main.py"]