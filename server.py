from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import random
from OTP_binary_chiffre import dechiffOTP, chiffOTP

key_filename = "OTP_binary"

def generate_OTP():

    f = open("OTP", "w")

    # generowanie klucza
    key = ""
    for i in range(2000):
        x = random.randint(0, 255)
        key += str(x)
        if i < 1999:
            key += " "

    f.write(key)
    f.close()


def generate_binary_OTP():

    f = open("OTP_binary", "w")

    # generowanie klucza
    key = ""
    for i in range(16000):
        x = random.randint(0, 128)
        key += str(x)+" "

    f.write(key)
    f.close()


def accept_incoming_connections():

    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Serwer: Podaj swoje imie i wcisnij enter.", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Serwer: Witaj %s! Wpisz quit aby wyjsc.' % dechiffOTP(name, key_filename)
    client.send(bytes(welcome, "utf8"))
    msg = "Serwer: %s has joined the chat!" % dechiffOTP(name, key_filename)
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        #quit = "quit" #tu zdeszyfrowac
        if msg != bytes(chiffOTP("quit", key_filename), "utf8"):                              ## chiffOTP("quit", key_filename):
            broadcast(msg, name + ": ")
        else:
            client.send(bytes(chiffOTP("quit", key_filename), "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("Serwer: %s has left the chat." % dechiffOTP(name, key_filename), "utf8"))
            break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)


clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1234
address = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(address)

if __name__ == "__main__":

    generate_OTP()
    generate_binary_OTP()
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()

