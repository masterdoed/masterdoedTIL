import TIL_backstage


#event data format: datetime|title|url|media|eventimlink|shopping

bs_url="https://backstage.info/veranstaltungen-2/alle-veranstaltungen"
bstage=TIL_backstage.Backstage()
bstage.readBackstage(bs_url)

