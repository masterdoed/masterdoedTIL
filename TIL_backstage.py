import os
import requests
from bs4 import BeautifulSoup


class Backstage:
	
	url=""

	def __init__(self):
		url=self.url

	def readBackstage(self,url):
		eventList=[]
		html=requests.get(url).text
		soup=BeautifulSoup(html, 'lxml')
		events=soup.find_all(class_='teaser-item event')
		


	


