#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

answer_code = {
    "Trying":"SIP/2.0 100 Trying\r\n",
    "Ringing":"SIP/2.0 180 Ringing\r\n",
    "Ok":"SIP/2.0 200 OK\r\n",
    "Bad Request":"SIP/2.0 400 Bad Request\r\n",
    "Methon Not Allowed":"SIP/2.0 405 Method Not Allowed\r\n"}

#SIP_type = {
#    "INVITE":"SIP/2.0 100 Trying\r\n" + "SIP/2.0 180 Ringing\r\n" +
#            "SIP/2.0 200 OK\r\n"
#    "BYE":
#    "ACK":
#}

class SIPServer(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print("El cliente nos manda " + line.decode('utf-8'))

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break
    def msg_answer_constructor(self,sip_type):
        if sip_type == "INVITE":
            pass
    pass


if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    if len(sys.argv) != 4:
        sys.exit("Usage: python3 client.py method receiver@IP:SIPport")
    port = int(sys.argv[2])
    audio = sys.argv[3]
    serv = socketserver.UDPServer((sys.argv[1], port), SIPServer)
    print("Listening...")
    serv.serve_forever()
