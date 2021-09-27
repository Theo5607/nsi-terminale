import socket

host, port = ('', 5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("serveur démarré")

while True:
    socket.listen(5)
    conn, adress = socket.accept()
    print("en écoute")
    
    data = socket.recv(1024)
    data = data.decode("utf8")
    
conn.close()
socket.close()