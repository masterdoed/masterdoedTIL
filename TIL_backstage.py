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
		#get all event DIV tags
		events=soup.find_all(class_='teaser-item event')
		#get event media
		# TO BE DONE (<img>)
		#get event titles
		for event in events:
			#get event title + link
			titles=event.findAll('h2', class_='pos-title')
			for title in titles:
				eventNames=title.findAll('a')
				for eventName in eventNames:
					print(eventName)
			#get event date
			datetimes=event.findAll('div', class_='element-date')
			for datetime in datetimes:
				dts=datetime.findAll('p')
				for dt in dts:
					print(dt)





	


