import glob
import os

if os.path.exists('dictionary.json'):
	os.remove('dictionary.json')									#make sure you won't append new data to old one

try:
	with open('dictionary.json', 'a') as dic:							#open base file
		for file in glob.iglob('*.json'):								#serch for .json files 
			if file.find('_') > 0:										#take only those that have underscore somewhere in the middle of its name
				with open(file, 'r') as source:							#open each one of them
					[dic.write(line) for line in source.readlines()]	#write their contents to the base file
except e:
	print('An exception occurred', file=stderr)