import os
import requests
from bs4 import BeautifulSoup


class Backstage:

	url=""

	def __init__(self):
		self.url="https://backstage.info/veranstaltungen-2/alle-veranstaltungen/1"
		#https://backstage.info/veranstaltungen-2/alle-veranstaltungen/2

	def readBackstage(self,url):
		eventList=[]
		html=requests.get(url).text
		soup=BeautifulSoup(html, 'lxml')
		#get all event DIV tags
		events=soup.find_all(class_='teaser-item event')
		
		#process and transform event data to dict
		for event in events:
			eventDict={}
			#get event media
			# TO BE DONE (<img>)
			#get event title
			titles=event.findAll('h2', class_='pos-title')
			for title in titles:
				eventNames=title.findAll('a')
				for eventName in eventNames:
					eventDict['eventname']=eventName.text
			#get weekday, date, time
			datetimes=event.findAll('div', class_='element-date')
			for datetime in datetimes:
				dts=datetime.findAll('p')
				for dt in dts:
					datetime=dt.text
					dtSplit=datetime.split(",")
					weekday=dtSplit[0]
					date=dtSplit[1].split("Beginn:")[0]
					time=dtSplit[1].split("Beginn:")[1]
					eventDict['weekday']=weekday.strip()
					eventDict['date']=date.strip()
					eventDict['time']=time.strip()
			#get event tags
			itemtags=event.findAll('div', class_='element-itemtag')
			for itemtag in itemtags:
				genre=""
				tags=itemtag.findAll('li')
				i=0
				for t in tags:
					if len(tags)<=1:
						genre=t.text
					else:
						genre=genre+","+t.text
				if genre=="":
					genre="unknown"
					eventDict['itemtag']=genre
				else:	
					eventDict['itemtag']=genre

			#add eventDict to eventList
			eventList.append(eventDict)

		return eventList

	def printEvents(self,eventList):
		for item in eventList:
			#result = item['itemtag'] + "|" + item['weekday'] + "|" + item['date'] + "|" + item['time'] + "|" + item['eventname']
			print(item['itemtag'])
			






	


