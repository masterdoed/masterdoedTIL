from unittest import result
import requests
import time
import random
import decimal
import json
import argparse
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from re import search
import urllib3



# Default function to load an given URL in a webobject for further processing
def getURL(url):
	## initialize some settings for http requests
	requests.packages.urllib3.disable_warnings()
	useragent = UserAgent()
	results_obj = {}
	referrer = 'https://www.github.com/'
	page = 1
	startnum = 0
	session = requests.session()
	response = session.get(url)
	cookies = session.cookies.get_dict()
	headers = {'user-agent': useragent.random, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Referer': referrer,'Upgrade-Insecure-Requests': '1'}
	for k, v in cookies.items():
		headers[k] = v
	webobject = BeautifulSoup(requests.get(url, headers=headers, verify=False).content, "lxml")
	return webobject


# Function to crawl metal.de for new black metal releases links
# links are stored in an array resultList and returned
def getBMReleaseLinks(webobject):
    resultList=[]
    ## metal.de stores all release reviews in a div container called "reviews", let's fetch it
    resultbody = webobject.find('div', {'class': 'reviews'})
    if len(resultbody) >= 1:
        ## all single reviews can be fetched by looking for div class card
        items=resultbody.find_all(class_="card")
        for i in items:
            links=i.find_all('a', href=True)
            for l in links:
                resultList.append(l['href'])
    return resultList



# Function to follow each release link, retrieve metadata and store in dictList
def getBMReleaseMeta(resultList):
	dictList=[]
	for i in resultList:
		dictList.append(parseBMReleaseMeta(i))
	return dictList


# Function to parse a resultList url and convert it to a metList item
# metaDict structure: URL ALBUM BAND GENRE DATE LABEL
def parseBMReleaseMeta(url):
	metaDict={}
	webobject=getURL(url)
	resultbody=webobject.find('div', {'class': 'article-info card'})
	if len(resultbody) >= 1:
		headings=resultbody.findChildren('h3')
		heading=headings[0]
		album=heading.get_text().split(" - ")[1]
		metaDict["url"]=url
		metaDict["album"]=album
		tables=resultbody.findChildren('table')
		myTable=tables[0]
		rows=myTable.findChildren('tr')
		metaDict["band"]=rows[0].findChildren('td')[0].string
		metaDict["genre"]=rows[3].findChildren('td')[0].string
		metaDict["date"]=rows[6].findChildren('td')[0].string
		metaDict["label"]=rows[7].findChildren('td')[0].string
		## TASK: GET SHOPPING DETAILS ADD AFFILIATE LINK
	return metaDict

# Function to store release information and metadata to database
def storeRelease(metaList):    
    ## TASK: TBD
	return metaList

# Function to add and/or retrieve an affiliate link 
def getAffiliate(name):
	## TASK: TBD
	return name

# simple class for printing dict in plaintext
def printer(dict):
	for d in dict:
		print(d["band"], d["album"], d["date"], d["label"], d["url"], )

# simpel class for printing dict as html
def htmlPrinter(dict):
	print("<html><head><title>BLACK METAL RELEASES</title></head><body>")
	print("<table>")
	for d in dict:
		print("<tr>")
		print("<td>")
		print(d["band"])
		print("</td>")
		print("<td>")
		print(d["album"])
		print("</td>")
		print("<td>")
		print(d["date"])
		print("</td>")
		print("<td>")
		print(d["label"])
		print("</td>")
		print("<td>")
		print(d["url"])
		print("</td>")
		print("</tr>")
	print("</table>")
	print("</html>")


# main function
def main():
	printer(getBMReleaseMeta(getBMReleaseLinks(getURL("https://www.metal.de/reviews/genre/black-metal/"))))
	#htmlPrinter(getBMReleaseMeta(getBMReleaseLinks(getURL("https://www.metal.de/reviews/genre/black-metal/"))))
# main caller
if __name__ == '__main__':
	main()
