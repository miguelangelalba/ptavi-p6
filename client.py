#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.
def msg_constructor(sip_type,login):
# Dirección IP del servidor.
    msg_to_send = sip_type + " sip:" + login + " SIP/2.0" + "\r\n"
    return msg_to_send

def comunication (server,port,sip_type,login):
    # Contenido que vamos a enviar
    LINE = '¡Hola mundo!'

    # Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        my_socket.connect((server, port))

        print("Enviando: " + LINE)
        msg_to_send = msg_constructor(sip_type,login)
        my_socket.send(bytes(msg_to_send, 'utf-8') + b'\r\n')
        data = my_socket.recv(1024)

        print('Recibido -- ', data.decode('utf-8'))
        print("Terminando socket...")

    print("Fin.")

if __name__ == '__main__':

    if len(sys.argv) != 3:
        sys.exit("Usage: python3 client.py method receiver@IP:SIPport")

    sip_type = sys.argv[1].upper()
    login = sys.argv[2][:sys.argv[2].find("@")]
    server = sys.argv[2][sys.argv[2].find("@") + 1:sys.argv[2].find(":")]
    port = int(sys.argv[2][sys.argv[2].find(":") + 1:])
    comunication(server,port,sip_type,login)
