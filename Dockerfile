# Imagem base do Python
FROM python:3.11-slim

# Diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos do seu projeto para o contêiner
COPY . /app

# Executa o arquivo principal do projeto
CMD ["python", "main.py"]