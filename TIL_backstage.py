import os
import requests
from bs4 import BeautifulSoup

#DATAMODEL FOR eventDict
#event data format: source|datetime|title|url|media|eventimlink|shopping


class Backstage:

	eventList=[]
	url="https://backstage.eu/veranstaltungen.html?p="

	#URL Iterator. Go through all pages of backstage events
	def iterator (self):
		i=1
		el=self.eventList
		for i in range(30):
			u=self.url + str(i)
			el.append(self.readBackstageEvent(u))
		return el

	#extract events from backstage events website
	def readBackstageEvent(self,u):
		#url_html will hold the html output of the url request
		url_html=requests.get(u).text
		#url_soup will hold the parsable html output as lxml
		url_soup=BeautifulSoup(url_html, 'lxml')
		#url_events will hold all event entries per page based on html class
		url_events=url_soup.find_all(class_='item product product-item')
		#process and transform event data to dict
		for event in url_events:
			eventDict={}
			#set source
			eventDict['source']='Backstage'
			#extract title from events
			#event_titles will hold all event titles per page
			event_titles=event.findAll('a', class_='product-item-link')
			for title in event_titles:
				eventDict['title']=title.text.translate({ord('\t'): None}).translate({ord('\n'): None})
				eventDict['url']=title['href']
			#extract datetime from event
			event_datetimes=event.findAll('strong', class_='product name product-item-name eventdate')
			for event_dt in event_datetimes:
				eventDict['datetime']=event_dt.text
		return eventDict


	





	


