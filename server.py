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

BUFFER_SIZE = 512
PORT = args.port

class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

# # #

signal.signal(signal.SIGINT, exit_handler)

# # #

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
			
			[connected_socket.sendall("\nThe word {} can be translated from polish to english and means {}\n".format(color.RED + i['pol'] + color.END, color.BLUE + i['eng'] + color.END).encode()) for i in database if i['pol'] == word]
			[connected_socket.sendall("\nThe word {} can be translated from english to polish and means {}\n".format(color.RED + i['eng'] + color.END, color.BLUE + i['pol'] + color.END).encode()) for i in database if i['eng'] == word]
			
			data = connected_socket.recv(BUFFER_SIZE)
			
		connected_socket.shutdown(socket.SHUT_RDWR)
		connected_socket.close()   
	sock.close()
