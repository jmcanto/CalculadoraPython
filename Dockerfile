FROM alpine:3.12
RUN apt-get update &&
    apt-get install -y python

WORKDIR /calculadora
COPY .  /calculadora