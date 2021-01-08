import os
import requests
from bs4 import BeautifulSoup

#DATAMODEL FOR eventDict
## media
## link
## eventname
## link
## weekday
## date
## time
## itemtag


class Backstage:

	url=""
	myGenres=[]

	def __init__(self):
		self.url="https://backstage.info/veranstaltungen-2/alle-veranstaltungen/1"
		#https://backstage.info/veranstaltungen-2/alle-veranstaltungen/2

	#iterate over pagination if there is more than one page with events
	def iterateURL(self,url):
		urllist=[]

		return urllist 

	#filter item tags for interesting genres
	def filterGenres(self, myGenres, eventList):

		return eventlist

	#extract events from backstage events website
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
					link="https://backstage.info"+eventName['href']
					eventDict['link']=link
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
			if len(itemtags) > 0:
				for itemtag in itemtags:
					genre=""
					i=0
					tags=itemtag.findAll('li')
					for t in tags:
						if i==0:
							genre=t.text
						else:
							genre=genre+","+t.text
					eventDict['itemtag']=genre
			else:
				eventDict['itemtag']="unknown"
			#add eventDict to eventList
			eventList.append(eventDict)

		return eventList

	def printEvents(self,eventList):
		for item in eventList:
			result = item['itemtag'] + "|" + item['weekday'] + "|" + item['date'] + "|" + item['time'] + "|" + item['eventname'] + "|" + item['link']
			print(result)






	


