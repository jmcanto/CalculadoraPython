FROM alpine:3.12
RUN apt-get update &&
    apt-get -y install python

WORKDIR /calculadora
COPY .  /calculadora