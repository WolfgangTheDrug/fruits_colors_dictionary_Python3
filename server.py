import argparse, socket, sys
import struct, signal
import glob, os

parser = argparse.ArgumentParser(description='Pol-Eng Fruits & Colors Dictionary Server')
parser.add_argument('port',
					metavar='port',
					type=int)
args = parser.parse_args()

# # #

def exit_handler(signum, frame):
	raise SystemExit('\nThe programme has been closed.')

# # #

BUFFER_SIZE = 512
PORT = args.port

# # #

signal.signal(signal.SIGINT, exit_handler)

# # #

with socket.socket() as sock:
	sock.bind(('', PORT))
	sock.listen()

	while True:
		connected_socket, address = sock.accept()
		data = connected_socket.recv(BUFFER_SIZE)
		print('Connected with ', address)

		while data: 
			request = data.decode()
			print('Word requested: ', request)
			
			answer = 'I\'ve received: ' + request
			connected_socket.sendall(answer.encode())

			data = connected_socket.recv(BUFFER_SIZE)
			
		connected_socket.shutdown(socket.SHUT_RDWR)
		connected_socket.close()   
	sock.close()
