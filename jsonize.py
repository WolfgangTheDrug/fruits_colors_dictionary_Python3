import argparse

parser = argparse.ArgumentParser(
	description='Pol-Eng Fruits & Colors Dictionary API formatter. Takes a file, (if needed) translates it to the standard form: pl - eng and converts it into a JSON format database.')
parser.add_argument(
	'file_name', 
	type=str,
	help='Name of the file to be JSONized. The file has to exist in the current directory.')
args = parser.parse_args()

with open(args.file_name, 'r') as source:
	source_line = source.readline()
	while source_line:
		print(source_line)
		source_line = source.readline()

print('Reading file ' + args.file_name + ' completed')