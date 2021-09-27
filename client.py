import socket

host, port = ('localhost', 5566)

try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((host, port))
    print("Client connecté")
except ConnectionRefusedError:
    print("connexion failed")
    
    data = "yo matvei"
    data = data.encode("utf8")
    socket.sendall(data)
finally:
    socket.close()