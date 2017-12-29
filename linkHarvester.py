#!/usr/bin/python

from bs4 import BeautifulSoup
import re
import requests
import time
import datetime

# set some variables...
linkFileBase = "/home/jeffc/code-projects/Python-experiments/BuyMedia/harvestedLinks"
fileDate = datetime.datetime.now()
linkFile = linkFileBase + "_" + fileDate.strftime("%y-%m-%d-%H-%M-%S")

#url = raw_input("Enter a website to extract the URL's from: ")

urls = [ 'www.irishexaminer.com', 'www.thesun.ie', 'www.joe.ie', 'www.independent.ie', 'www.irishmirror.ie']
harvestedLinks = []

with open(linkFile, 'a+') as linkfile:
	for url in urls:
		r  = requests.get("http://" +url)
		data = r.text
		soup = BeautifulSoup(data)
#		links = soup.find_all('a')
#		for link in list(set(links)):
		# here we have a full list of a tags found, with more than the href
		for link in soup.find_all('a'):
			# here we extract the href
    			href = str(link.get('href'))
			
			# need some sort of check here to see if the url domain is present
			# if not, prepend to href
			if url in href:
				print "OK! nothing to fix.\n"
			else: 
				href = "http://" + url + href
				print "Fixed noncanonical link " + href + "\n"			

			# here, check to see if the link is likely to be an article
			# e.g. - ends in .html, has a 5-or-more digit number in the string
			# and if so, save the link. Otherwise skip it. 
			if 'html' in href:
				# many articles end in .html, save these
				harvestedLinks.append(href)
			elif re.findall(r'[0-9]{5,8}', href):
				# many articles also include a long numeric string
                                harvestedLinks.append(href)
			else:
				print 'Skipping ' + href + ".\n"
	# the list of harvested links we now have is full of duplicates, so we use set to remove them
	for hL in list(set(harvestedLinks)):
		linkfile.write(hL + '\n')

linkfile.close()




# To-do: 
# dedupe the list of links 
# save the file to s3 (if desired, now writing to local disk)
#
# then...
# something to read file from s3, extract urls, 
# pass them to aylien API, get JSON results, store relevant data into new s3 store
# (aylienator.py does most of this now)
#
# then...
# read new s3 data store, merge documents by publication
# derive and store a profile summary from all the docs 
# (profileMaker.py heading in this direction)
