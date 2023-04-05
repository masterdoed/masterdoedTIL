import TIL_backstage


#event data format: datetime|title|url|media|eventimlink|shopping


bs=TIL_backstage.Backstage()
el=bs.readBackstageEvent()

for item in el:
	result = item['datetime'] + "|" + item['title'] + "|" + item['url'] 
	print(result)
