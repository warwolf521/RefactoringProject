# Usa imagen base de Python
FROM python:3.11-slim

# Variables de entorno
ENV FLASK_APP=main.py
ENV FLASK_RUN_PORT=3000
ENV FLASK_RUN_HOST=0.0.0.0

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos al contenedor
COPY . /app

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Ejecutar script para inicializar la base de datos
RUN python crear_db.py

# Exponer el puerto de Flask
EXPOSE 3000

# Comando para lanzar la app
CMD ["python", "main.py"]