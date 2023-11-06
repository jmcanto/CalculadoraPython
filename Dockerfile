FROM alpine:latest

# después de actualizar y instalar python se borra la caché de los paquetes
RUN apk update && apk add python3 && rm -rf /var/cache/apt/*

WORKDIR /calculadora
COPY .  /calculadora
ENTRYPOINT ["python", "./calculadora.py"]