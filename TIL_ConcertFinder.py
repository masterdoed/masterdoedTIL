import TIL_backstage


#event data format: datetime|title|url|media|eventimlink|shopping



bstage=TIL_backstage.Backstage()
bstage.printEvents(bstage.readBackstage(bstage.url))

