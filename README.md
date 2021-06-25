# Pol-Eng Fruits & Colors Dictionary with Python3 server-client


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

This file structure allows for an easy and scallable mechanism of widening the range of words the programme.

## Resources

The translations were taken from:
* [fruits ](https://www.ingless.pl/artykul/owoce-w-jezyku-angielskim/)
* [colors ](https://speakin.pl/kolory-po-angielsku/)

and changed slighly.
