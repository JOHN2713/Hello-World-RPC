FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /RPC_FLASK

# Copiar los archivos
COPY rpc_server_flask.py .
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer los puertos
EXPOSE 5000 9000

# Comando para iniciar el servidor
CMD ["python", "rpc_server_flask.py"]
