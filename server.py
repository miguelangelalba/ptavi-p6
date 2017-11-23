#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os

answer_code = {
    "Trying":b"SIP/2.0 100 Trying\r\n\r\n",
    "Ringing":b"SIP/2.0 180 Ringing\r\n\r\n",
    "Ok":b"SIP/2.0 200 OK\r\n\r\n",
    "Bad Request":b"SIP/2.0 400 Bad Request\r\n\r\n",
    "Method Not Allowed":b"SIP/2.0 405 Method Not Allowed\r\n\r\n"
    }

SIP_type = {
    "INVITE":answer_code["Trying"] + answer_code["Ringing"] +
            answer_code["Ok"],
    "BYE":answer_code["Ok"],
    "ACK":answer_code["Ok"]
    }

class SIPServer(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    def handle(self):
        line = self.rfile.read().decode('utf-8').split(" ")
        if not line[0] in SIP_type:
            self.wfile.write(answer_code["Method Not Allowed"])
        elif line[0] == "ACK":
            aEjecutar = "./mp32rtp -i 127.0.0.1 -p 23032 < " + AUDIO
            print("ACK recibido ejecutando:", aEjecutar)
            os.system(aEjecutar)

        else:
            self.wfile.write(SIP_type[line[0]])
            print("El cliente nos manda " + line[0])


if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    if len(sys.argv) != 4:
        sys.exit("Usage: python3 client.py method receiver@IP:SIPport")
    port = int(sys.argv[2])
    AUDIO = sys.argv[3]
    serv = socketserver.UDPServer((sys.argv[1], port), SIPServer)
    print("Listening...")
    serv.serve_forever()
