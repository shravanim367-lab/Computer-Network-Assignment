import socket

HOST = "127.0.0.1"      # Localhost
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server is waiting for connection...")

conn, addr = server.accept()
print(f"Connected by {addr}")

message = conn.recv(1024).decode()

print("Message received from client:", message)

conn.send("Message received successfully!".encode())

conn.close()
server.close()