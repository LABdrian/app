# Usar una imagen base de Python
FROM python:3.11

# Establecer un directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios en el contenedor
COPY requirements.txt .
COPY ./app ./app

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt




#variables de entorno
ENV PYTHONPATH="${PYTHONPATH}:/app/app"

