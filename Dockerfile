FROM alpine:latest
env operacion = 3
env operador1 = 40
env operador2 = 656
# después de actualizar y instalar python se borra la caché de los paquetes
RUN apk update && apk add python3 && rm -rf /var/cache/apt/*

WORKDIR /calculadora
COPY .  /calculadora
CMD ["python", "./calculadora.py", "-o", $operacion, "-n1", $operador1, "-n2", $operador2]
