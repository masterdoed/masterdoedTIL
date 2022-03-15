from distutils.filelist import findall
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






# main function
def main():
	print(getBMReleaseLinks(getURL("https://www.metal.de/reviews/genre/black-metal/")))

# main caller
if __name__ == '__main__':
	main()
