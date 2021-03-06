import socket, os, signal, sys
import argparse
import json

parser = argparse.ArgumentParser(
	description="Pol-Eng Fruits & Colors Dictionary Client")
parser.add_argument(
	"host_port", 
	type=str,
	help="Host and port numbers separated by \":\"")
args = parser.parse_args()

# # #

def exit_handler(signum, frame):
	raise SystemExit("\nThe programme has been closed.")

def center(text, character=""):
	return ('{:' + character + '^50}').format(text)

def preamble(word):
	return "\n" + center("The following translations of the word \'{}\' {}have been found{}:").format(word, color.DARKCYAN + color.BOLD, color.END) + "\n" + color.PURPLE + color.UNDERLINE + center(" English - Polish ", "*") + color.END

def word_not_found(word):
	return "\n" + color.RED + color.UNDERLINE + center(" Alert ", "*") + color.END + "\n" + center("Any translation of the word \'{}\' was ".format(word) + color.RED + color.UNDERLINE + "not found" + color.END)

def strip(array_of_str):
	tmp = []
	[tmp.append(el.strip()) for el in array_of_str]
	return tmp

def listize(string):
	tmp = string.split(",")
	tmp = strip(tmp)
	return tmp
	
# # #

BUFFER_SIZE = 2048
HOST, PORT = args.host_port.split(":")
PORT = int(PORT)
class color:
	PURPLE = "\033[95m"
	CYAN = "\033[96m"
	DARKCYAN = "\033[36m"
	BLUE = "\033[94m"
	GREEN = "\033[92m"
	YELLOW = "\033[93m"
	RED = "\033[91m"
	BOLD = "\033[1m"
	UNDERLINE = "\033[4m"
	END = "\033[0m"

# # #

signal.signal(signal.SIGINT, exit_handler)

try:
	if ":" not in args.host_port:
		print(
			"Error: wrong format of host_port variable. Check --help for help!" 
			, file=stderr
		)
		raise IOError
except IOError as IOErr:
	sys.exit(1)

# # #

with socket.socket() as sock:
	sock.connect((HOST, PORT))
	while(True):
		request = input("\n>")
		requests = listize(request)
		for request in requests:
			sock.sendall(request.encode())
			response = sock.recv(BUFFER_SIZE).decode()
			
			if response == "x":
				print(word_not_found(request)) 
			else:
				response = "[" + response.replace("'",'"') + "]"
				response = json.loads(response)
				print(preamble(request))
				for position in response:
					translations = list(position.values())
					print(center("{} - {}".format(translations[0], translations[1])))
	sock.shutdown(socket.SHUT_RDWR)
	sock.close()

# # # 