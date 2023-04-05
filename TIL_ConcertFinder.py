import TIL_backstage


#event data format: source|datetime|title|url|media|eventimlink|shopping


bs=TIL_backstage.Backstage()
el=bs.iterator()

for item in el:
	result = item['source'] + " | " + item['datetime'] + " | " + item['title'] + " | " + item['url'] 
	print(result)
