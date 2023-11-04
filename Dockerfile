FROM alpine:latest

WORKDIR /calculadora
COPY .  /calculadora

RUN apk  --update add python3