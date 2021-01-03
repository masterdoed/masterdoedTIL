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
			eventDict={}
			#get event title + link
			titles=event.findAll('h2', class_='pos-title')
			for title in titles:
				eventNames=title.findAll('a')
				for eventName in eventNames:
					eventDict['eventName']=eventName.text
			#get event date
			datetimes=event.findAll('div', class_='element-date')
			for datetime in datetimes:
				dts=datetime.findAll('p')
				for dt in dts:
					eventDict['datetime']=dt.text
			eventList.append(eventDict)
		return eventList

	def printEvents(self,eventList):
		for item in eventList:
			result=eventList.pop()['datetime'] + "|" + eventList.pop()['eventName']
			print(result)





	


