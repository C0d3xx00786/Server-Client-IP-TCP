import socket
import getpass
import speedtest # Не работает без VPN
import psutil

name = getpass.getuser() # Получаем название Пк
IP = socket.gethostbyname(socket.getfqdn()) # Получаем Ip
st = speedtest.Speedtest(secure=True) # secure чтобы истользовать https вместо http

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Создаём сокет с протоколами IP и TCP
s.bind(('', 65432)) # Из за Ipv4 привязываем сокет к порту и хосту (Ip ставится стандартный 127.0.0.1)
s.listen() # Прослушка
conn, addr = s.accept() # Принятие подключения
print(f"Подкюченние от {addr}")

while True:
    st.get_best_server() # Нахождение лучшего сервера
    std = round(st.download() / 8388608, 2) # перевод из бит в Мбайт и округляет
    stu = round(st.upload() / 8388608, 2)
    ping = st.results.ping

    vmt = round(psutil.virtual_memory().total / 1073741824, 2)
    vmu = round(psutil.virtual_memory().used / 1073741824, 2)

    list = str([name, IP, std, stu, ping,
                psutil.cpu_percent(3), psutil.cpu_freq().max,
                psutil.cpu_freq().current, vmt,
                vmu, psutil.disk_usage('/').percent]) # Данные которые мы должны отправить клиенту
    conn.sendall(list.encode()) # Отправить данные клиенту