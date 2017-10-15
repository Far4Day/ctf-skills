#!/usr/bin/python3
# This code don't capture the flag...Not Yet - Bugnario - Hackaflag 2017

import itertools, socket

def bin_sequence(number):
	return list(map(''.join, itertools.islice(itertools.product('01', repeat=len(bin(number)[2:])), 0, number)))

def sanitize_list(list_binaries):
	return list(filter(lambda k: '11' in k, list_binaries))

server = "138.197.10.170"
port = 8947

connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect((server,port))
print(connection.recv(2048).decode())
connection.send('start'.encode())
print(connection.recv(1024).decode())
data=(connection.recv(1024).decode())
final = 0
while True:
	print(data, end=" ")
	challenge = int(data.split(':')[1].split('\n')[0])
	final = challenge - len(sanitize_list(bin_sequence(challenge)))
	print(final)
	s.send(str(final).encode())
	print(connection.recv(128).decode(),end=' ')
	data = (connection.recv(512).decode())
