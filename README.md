# Pol-Eng Fruits & Colors Dictionary with Python3 server-client


## Add your own list of words!

The program has been written to support user defined wordlists. 
Here's the quick guide on how to do it:
1. in the working directory create a file called `dictionary_*.txt`
1. write there the content of your wordlist. It should has the following format: `(word *[-=:>]+ * word\n)*` where one word is in english and the second one is in polish.
1. go to the working directory and paste `python3 jsonize.py dictionary_*.txt` and add `-pl` flag if your source file has translation direction pol-eng.
	* Don't worry if you messed up! You can JSONize your file as many times as you wish 😉
1. repeat the steps above with all wordlists you want to add
1. finally, paste `python3 combine_json_dictionaries.py`
	* Don't worry if you messed up! You can JSONize your file as many times as you wish 😉

## Files

__server.py__/__client.py__ - files conducting the dialogue. 
Clients send a request to the server and his response consists of every translation possible for a given request.
This means that ambiguos words will be translated both to polish and english.
If the requested word isn't in the database, client receives an error message instead.

__jsonize.py__ - converter from \*.txt to \*_\*.json files.

__combine_json_dictionaries.py__ - \*_\*.json files combiner.

__\*.txt__ - raw word lists.

__\*_\*.json__ - standard JSON/MongDB database inheriting its name from the .txt file it is based upon.

__dictionary.json__ - complete dictionary combining every \*_\*.json subdatabases.

This file structure allows for an easy and scallable mechanism of widening the range of words the program.

## Resources

The translations were taken from:
* [fruits ](https://www.ingless.pl/artykul/owoce-w-jezyku-angielskim/)
* [colors ](https://speakin.pl/kolory-po-angielsku/)
* [colorfull terminal](https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal)
and changed slighly.
