FROM alpine:latest

# después de actualizar y instalar python se borra la caché de los paquetes
RUN apk update && \
apk add --no-cache python3 py3-pip && \
python3 -m ensurepip && \
pip3 install --no-cache --upgrade pip setuptools

WORKDIR /calculadora
COPY .  /calculadora

#variables de entorno a utilizar
ENV operacion 3
ENV operador1 40
ENV operador2 656

ENTRYPOINT ["python3","./calculadora.py"]