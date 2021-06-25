import argparse, socket, sys
import struct, signal
import glob, os

DEFAULT_MAX_MESSAGE_LENGTH, DEFAULT_NUMBER_OF_MESSAGES, DEFAULT_MAX_NUMBER_OF_MESSAGES, BUFFER_SIZE = 140, 20, 99, 1024

parser = argparse.ArgumentParser(description='Simple notice board')
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

signal.signal(signal.SIGINT, handler_programme)

# # #

with socket.socket() as sock:
	sock.bind(('', port))
	sock.listen()

	messages = get_messages_from_files()

	while True:
		connected_socket, address = sock.accept()
		data = connected_socket.recv(BUFFER_SIZE)
		print('Connected with ', address)

		if not data:
			for message in messages:
				message_to_send = '%x\r\n%s' % (len(message), message)
				encodedData = message_to_send.encode()
				connected_socket.sendall(encodedData)
			print('Data has been sent to ', address)
		else:
			message_from_client = data.decode()[:args.c] # msg is what came from client, cut the excess if needed
			messages[:0] = message_from_client # add msg at the front of msgs
			messages = messages[:args.n] # if too big, cut the excess
			print('Data has been collected from ', address)

		connected_socket.shutdown(socket.SHUT_RDWR)
		connected_socket.close()   
	sock.close()
