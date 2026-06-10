import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 65432)) # Подключение к определённому серверу по Ip и порту
print("Происходит сбор данных с сервера, подождите")

while True:
    data = s.recv(1024) # Принятие данных от сервера
    list = str(data)[3:-2].split(", ") # Избавляемся от лишних символов
    os.system('cls') # Очищаем консоль
    print(f"[--------Название ПК: {list[0]}--------]")
    print(f"[----------IP: {list[1]}----------]")
    print(f"[--Скорость скачивания: {list[2]} Мбайт/сек--]")
    print(f"[---Скорость загрузки: {list[3]} Мбай/сек---]")
    print(f"[------------Ping: {list[4]} мс------------]")
    print(f"[---CPU: {list[5]} %; Max: {list[6]} Mhz;---]")
    print(f"[--------Current: {list[7]} Mhz--------]")
    print(f"[----Опер. память: {list[8]} Gb; {list[9]} Gb----]")
    print(f"[------------Disk: {list[10]} %------------]")