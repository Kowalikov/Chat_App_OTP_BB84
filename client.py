from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from OTP_binary_chiffre import dechiffOTP, chiffOTP

key_filename = "OTP"

def receive():
    while True:
        try:
            msg_user = client_socket.recv(BUFSIZ).decode("utf8")
            user, msg = msg_user.split(": ")
            if user == "Serwer":
                msg_list.insert(tkinter.END, user + ": " + msg)
            else:
                msg_dechiff = dechiffOTP( msg, key_filename)
                msg_list.insert(tkinter.END, dechiffOTP(user, key_filename) + ": " + msg_dechiff)

        except OSError:
            break

def send(event=None):

    msg = my_msg.get()
    my_msg.set("")  # czysci pole gdzie wpisujemy wiadomosc
    if msg == "quit":
        client_socket.close()
        app.quit()
    else:
        if len(msg) < 2000:
            msg_chiffr = chiffOTP( msg, key_filename)
            client_socket.send(bytes(msg_chiffr, "utf8"))
        else:
            err_com = "Wiadomość powyżej 2000 znaków"
            client_socket.send(bytes(err_com, "utf8"))



def on_closing(event=None):
    my_msg.set("quit")  # zamkniecie okna X (w prawym gornym rogu) = wysyla za nas quit
    send()


# To dotyczy samego okna z apką
app = tkinter.Tk()

app.title("ChatApp")

messages_frame = tkinter.Frame(app)
my_msg = tkinter.StringVar()  # For the messages to be sent.
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(app, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(app, text="Send", command=send)
send_button.pack()

app.protocol("WM_DELETE_WINDOW", on_closing)

# Laczenie z serverem

HOST = input('Enter host: ')  # wpisujemy 127.0.0.1; dla drugiego uzytkownika na tym samym kompie 0.0.2 itd
PORT = 33000

BUFSIZ = 1234
address = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(address)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()