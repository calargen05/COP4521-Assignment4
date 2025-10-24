import socket
import sys
import os
import time

def recv_message(sock, buffer):
    newline_index = buffer.find('\n')


n = len(sys.argv)
if (n != 3):
    print("Usage: server_name port")
    exit()

s = socket.socket()

try:
    s.connect((sys.argv[1], int(sys.argv[2])))
except socket.error as errorMessage:
    print(f'failed to connect. [{errorMessage}]')
    exit()

beginningMsg = s.recv(1000)
print(beginningMsg.decode())
userPrompt = s.recv(1000)
user = input(userPrompt.decode())
print(f"Sending username: {user}")
try:
    s.send(user.encode())
except _:
    print("Socket sending error for username")

welcomeMsg = s.recv(1000)
print(welcomeMsg.decode())

while True:
    promptMsg = s.recv(1000)
    cmd = input(promptMsg.decode())
    s.send(cmd.encode())
    if cmd == "exit" or cmd == "quit":
        goodByeMsg = s.recv(1000)
        print(goodByeMsg.decode())
        s.close()
        exit()
