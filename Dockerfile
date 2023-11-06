FROM alpine:latest

# después de actualizar y instalar python se borra la caché de los paquetes
RUN apk update && apk add python3 && rm -rf /var/cache/apt/*

WORKDIR /calculadora
COPY .  /calculadora
<<<<<<< HEAD
ENTRYPOINT ["python", "./calculadora.py"]
=======
>>>>>>> 57639672d06bdbeefa33f7e44c6c0e3bcb14c3c7
