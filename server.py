import socket
import sys
from tkinter import *

def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = port_form.get()
        s=socket.socket()
    except socket.error as msg:
        print("Socket creation error found " + str(msg))

def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port : " + str(port))

        s.bind((host,port))
        s.listen(5)


    except socket.error as msg:
        print("Socket binding error found " + str(msg) + " \n retrying.........")
        bind_socket()

def socket_accept():
    conn,address = s.accept()
    print("connetion established! |"+ "IP "+ address[0] + "| Port : " + str(address[1]))
    send_commands(conn)
    conn.close()

#ki korte cai
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()






















