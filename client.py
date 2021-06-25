import socket, os, signal, sys
import argparse

parser = argparse.ArgumentParser(
	description='Pol-Eng Fruits & Colors Dictionary Client')
parser.add_argument(
	'host_port', 
	type=str,
	help='Host and port numbers separated by ":"')
args = parser.parse_args()

# # #

def exit_handler(signum, frame):
	raise SystemExit('\nThe programme has been closed.')

# # #

BUFFER_SIZE = 512
HOST, PORT = args.host_port.split(":")
PORT = int(PORT)

# # #

signal.signal(signal.SIGINT, exit_handler)

try:
	if ':' not in args.host_port:
		print(
			'Error: wrong format of host_port variable. Check --help for help!' 
			, file=stderr
		)
		raise IOError
except IOError as IOErr:
	sys.exit(1)

# # #

with socket.socket() as sock:
	sock.connect((HOST, PORT))
	try:
		odp = input(">")
		while(odp):
			sock.sendall(odp.encode())
			odp = sock.recv(256)
			print(odp.decode())
			odp = input(">") 
	except EOFError:
		sock.shutdown(socket.SHUT_RDWR)
	sock.close()

# # # 