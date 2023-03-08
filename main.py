# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1234  # The port used by the server


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = input("Enter message to send: ")
        s.sendall(message.encode())
        data = s.recv(1024)

    print('Received', repr(data.decode()))

# Visit my page at https://www.schmid-johann.de
