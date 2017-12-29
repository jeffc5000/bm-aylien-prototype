#!/usr/bin/python
import json
import time
import datetime
import sys
from aylienapiclient import textapi

# set some variables...
APP_ID = "ea8f3c33"
APP_KEY = "340e5d36ec727c4f19ba6063477e8651"
analysisFileBase = "/home/jeffc/code-projects/Python-experiments/BuyMedia/aylienAnalysis"
fileDate = datetime.datetime.now()
analysisFile = analysisFileBase + "_" + fileDate.strftime("%y-%m-%d-%H-%M-%S")


with open(sys.argv[1], 'r') as uFile:
	# iterate through our file of URLs to process
	loopRun = 1
	for myUrl in uFile:
		print "Calling aylien with URL #" + str(loopRun) + ": " + myUrl + "\n"
		# instantiate aylien client and make API call
		client = textapi.Client(APP_ID, APP_KEY)
		combined = client.Combined({
  		  'url': myUrl, 'endpoint': ["entities", "concepts", 
		  "classify/iab-qag", "classify/iptc-subjectcode", "sentiment",
		  "hashtags"]
	 	})

                with open(analysisFile, 'a+') as aFile:
                        aFile.write("URL: " + myUrl + "\n")
			# using for debugging...
			for result in combined["results"]:
				aFile.write(result["endpoint"], ":", result["result"], "\n")
                	        aFile.write("==========\n")

		# dump the JSON object returned from the call - probably not necessary
		# but I wanted to see these w/o the unicode 'u' identifier in the data.
		#jsonObj = json.dumps(combined)
		#with open(analysisFile, 'a+') as aFile:
		#	aFile.write("URL: " + myUrl + "\n")
		#	aFile.write("JSON: " + jsonObj + "\n")
		#	aFile.write("==========\n")
			print "Wrote record for URL " + myUrl + "\n"
		time.sleep(6)
		aFile.close()
		loopRun+=1

uFile.close()
