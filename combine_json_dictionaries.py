import glob
import os
import sys

if os.path.exists('dictionary.json'):
	os.remove('dictionary.json')													#make sure you won't append new data to old one

DUMMY_EOF = '\t{\n\t\t\"eng\": \"\",\n\t\t"pol": \"\"\n\t}\n'						#quick solution to all json library problems

try:
	with open('dictionary.json', 'a') as dic:										#open base file
		dic.write('[\n')
		for file in glob.iglob('*.json'):											#serch for .json files 
			if file.find('_') > 0:													#take only those that have underscore somewhere in the middle of its name
				with open(file, 'r') as source:										#open each one of them
					[dic.write('\t{}'.format(line)) for line in source.readlines()]	#write their contents to the base file
		dic.write(DUMMY_EOF + ']')
except Exception as e:
	print('An exception occurred: {}'.format(e))