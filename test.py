import socket
from functions import *


def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

ip = get_ip()
print("Adresse IP :", ip)
post("https://serveur-api-xw0q.onrender.com/save", {"ip" : ip})