#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.
def msg_constructor(sip_type):
# Dirección IP del servidor.
def comunication (server,port,sip_type,login):

    #SERVER = 'localhost'
    #PORT = 6001

    # Contenido que vamos a enviar
    LINE = '¡Hola mundo!'

    # Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        my_socket.connect((SERVER, PORT))

        print("Enviando: " + LINE)
        my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
        data = my_socket.recv(1024)

        print('Recibido -- ', data.decode('utf-8'))
        print("Terminando socket...")

    print("Fin.")

if __name__ == '__main__':

    if len(sys.argv) != 3:
        sys.exit("Usage: python3 client.py method receiver@IP:SIPport")

    sip_type = sys.argv[1]
    login = sys.argv[2][:sys.argv[2].find("@")]
    server = sys.argv[2][sys.argv[2].find("@") + 1:sys.argv[2].find(":")]
    port = sys.argv[2][sys.argv[2].find(":") + 1:]
