import argparse
import re # regular expressions
import os

parser = argparse.ArgumentParser(
	description='Pol-Eng Fruits & Colors Dictionary API formatter. Takes a file, (if needed) translates it to the standard form: pol - eng and converts it into a JSON format database.')
parser.add_argument(
	'file_name', 
	type=str,
	help='Name of the file to be JSONized. The file has to exist in the current directory.')
parser.add_argument(
	'-pl',
	action='store_true',
	help='Add this flag if your source file has translation direction `pol-eng`')
args = parser.parse_args()

# # #

def normalize_spaces(line):
	return re.sub(r' +', r' ', line)

def normalize_separators(line):
	return re.sub(r' [-=:>]+ ', r' - ', line)

def normalize_spaces_and_separators(line):
	return normalize_spaces(normalize_separators(line))

def reverse_translation_direction(line): # fully normalized
	return ' - '.join(line.split(' - ')[::-1]) if not args.pl else line 

def jsonize_line(line): # fully normalized and reversed if needed
	pol, eng = line.split(' - ')
	result = '\n\t\"pol\": \"{}\", \n\t\"eng\": \"{}\"\n'.format(pol.strip('\n'), eng.strip('\n'))
	return '{' + result + '},\n'

def apply_format(line):
	return jsonize_line(reverse_translation_direction(normalize_spaces_and_separators(line)))
# # #

SOURCE_NAME = args.file_name
SINK_NAME = args.file_name.split(".")[0] + '.json'	

# # #

try:
	with open(SOURCE_NAME, 'r') as source:
		with open(SINK_NAME, 'w') as sink:
			[sink.write(apply_format(line)) for line in source.readlines() if not re.match(r'[A-Z]\n|\n', line)]
except:
	print('File {} probably doesn\'t exist...'.format(SOURCE_NAME), file=stderr)
	sys.exit(1)
# # # TESTS # # #
 
"""----> test 1: reading file
with open(args.file_name, 'r') as source:
	source_line = source.readline()
	while source_line:
		print(source_line)
		source_line = source.readline()
"""

"""----> test 2: -pl arg
print ('Is pol ang: ' + str(args.pl)) # False if the flag isn't added and True when it is
"""

"""----> test 3: normalize_spaces_and_separators
lines = ['a - a', 'b-b', 'c-  c', 'd -d', 'e =e  e', 'f: f']
print(lines) # ['a - a', 'b-b', 'c-  c', 'd -d', 'e =e  e', 'f: f']
lines = [normalize_spaces_and_separators(line) for line in lines] 
print(lines) # ['a - a', 'b - b', 'c - c', 'd - d', 'e - e e', 'f - f']
"""

"""----> test 4: reading file the short way
with open(args.file_name, 'r') as source:
	[print(line) for line in source.readlines()]
"""

"""----> test 5: reverse_translation_direction
line = 'a - b'
print(reverse_translation_direction(line)) # b - a """

"""----> test 6: jsonize_line
line = 'kot - cat'
print(jsonize_line(line)) 
#{
#	"pol": "kot",
#	"eng": "cat"
#}
"""
