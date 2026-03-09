import socket

server = socket.socket(
    socket.AF_BLUETOOTH,
    socket.SOCK_STREAM,
    socket.BTPROTO_RFCOMM
)

port = 4

server.bind(("FC:6D:77:16:65:88", port))

server.listen(1)

print("Bluetooth server started")
print("Waiting for connection...")

client, address = server.accept()

print("Connected to:", address)

try:
    while True:
        data = client.recv(1024)

        if not data:
            break

        message = data.decode("utf-8")

        print("Received:", message)

except OSError:
    pass

print("Client disconnected")

client.close()
server.close()