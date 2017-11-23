#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys
from server import SIP_type, answer_code

def msg_constructor(sip_type,login,ip):
    msg = sip_type + " sip:" + login +"@" + ip + " SIP/2.0" + "\r\n"
    return msg

def comunication (server,port,sip_type,login):
    # Contenido que vamos a enviar

    # Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:

        my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        my_socket.connect((server, port))
        msg_to_send = msg_constructor(sip_type,login,server)
        my_socket.send(bytes(msg_to_send, 'utf-8') + b'\r\n')
        print("Enviando: " + msg_to_send)
        data = my_socket.recv(1024)
        print('Recibido -- ', data.decode('utf-8'))

        if data == SIP_type["INVITE"]:
            #Enviamos msg ack
            msg_to_send = msg_constructor("ACK",login,server)
            print("Enviando: " + msg_to_send)
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
