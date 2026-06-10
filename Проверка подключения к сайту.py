import socket
import time

port = 80 # Стандарт для браузера
name = input("Напишите к какому сайту вы хотите проверить подключение (Напишите его адресную строку): ")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Сокет создан с протоколом IP и TCP
    print("Сокет создан.")
    try:
        ip = socket.gethostbyname(name) # Получить Ip через адрес
        print(f"IP сайта {name} получен, его ip: {ip}")
        while True:  # Делаем бесконечную проверку подключения сайта с ожиданием в 5 минут
            try:
                s.connect((ip, port))  # Подключение по Ip и порту
                print("\n----------Подключение успешно!----------\n(Следующая проверка подключения через 5 минут.)")
                time.sleep(5)
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # Для новой проверки нужно создавать новый сокет, я не знаю почему
            except:
                print("Подключение не удалось.")
                break
    except:
        print("Не получилось получить Ip сайта.")
except:
    print("Невозможно создать сокет.")