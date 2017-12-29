#!/usr/bin/python
import datetime
import json
import sys
import time
from urlparse import urlparse

with open(sys.argv[1], 'r') as aylienFile:
        # iterate through our file of Aylien data to process
	# it's structured like so:
	#
	# URL: <url string>
	# JSON: <json object returned from Aylien for URL>
	# ==========
	# (next pair of URL and JSON) to infinity...or end of the file :)
	for s in aylienFile:

		# If line begins with URL, chop one way. 
		if s.startswith('URL: '):
			url = s.lstrip('URL: ')
			parsedUri = urlparse(url)
			webSite = parsedUri.netloc
			article = parsedUri.path
		
		# If line is aylien json, chop another.
		elif s.startswith('JSON: '):
			jsonstr = s.lstrip('JSON: ')
			parsedJson = json.loads(jsonstr)
			
		# Discard dashed lines

			print webSite, "\n"
			print article, "\n"
			print json.dumps(parsedJson, sort_keys=True, indent=4), "\n"
			#print parsedJson['results']['entities'], "\n"
			#print(parsedJson['entities']), "\n"

aylienFile.close()


