# imagen base
FROM python:3
# establece el directorio de trabajo
WORKDIR /usr/src/app
# Copiar la carpeta myapp a /usr/src/app
COPY ./myapp/ .
# instalacion de requerimientos y dependencias
RUN pip3 install -r requirements.txt
# incluir carpeta sync_files
#incluir subcarpetas public y private
# Abro el puerto 5000 del contenedor
EXPOSE 5000
# Establece el entrypoint
CMD ["python3", "./app.py"]
