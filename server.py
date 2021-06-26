import argparse, socket, sys
import signal
import glob, os
import json

parser = argparse.ArgumentParser(description='Pol-Eng Fruits & Colors Dictionary Server')
parser.add_argument('port',
					metavar='port',
					type=int)
args = parser.parse_args()

# # #

def exit_handler(signum, frame):
	raise SystemExit('\nThe programme has been closed.')

# # #

BUFFER_SIZE = 2048
PORT = args.port

# # #

signal.signal(signal.SIGINT, exit_handler)

# # #

try:
	with open('dictionary.json') as jsondata:
		database = json.load(jsondata)
except Exception as e:
	print(e)
	sys.exit(2)


with socket.socket() as sock:
	sock.bind(('', PORT))
	sock.listen()

	while True:
		connected_socket, address = sock.accept()
		data = connected_socket.recv(BUFFER_SIZE)
		print('Connected with ', address)

		while data: 
			word = data.decode()
			response = []
			[response.append(str(i)) for i in database if i['pol'] == word]
			[response.append(str(i)) for i in database if i['eng'] == word]
			connected_socket.sendall(','.join(response).encode()) if response else connected_socket.sendall('x'.encode())
			data = connected_socket.recv(BUFFER_SIZE)
			
		connected_socket.shutdown(socket.SHUT_RDWR)
		connected_socket.close()   
	sock.close()
