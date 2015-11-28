#!/usr/bin/env python
import requests
import lxml.html
import scraperwiki



train = "1", "2", "3"
for name in train:
    print name
    
url = 'https://www.yell.com/ucs/UcsSearchAction.do?keywords=pizza&location=southampton&scrambleSeed=833794509&pageNum'+name  
 
html = requests.get(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36"}).content
		
dom = lxml.html.fromstring(html)
		
premierLeagueData = []
		
x = 1
		
		
		
		
for row in dom.cssselect('div.businessCapsule-fle'):
	x += 1
		    
	id = x
	name = str(row.cssselect('div.businessCapsule--title')[0].text_content())
	telephone = str(row.cssselect('div.businessCapsule--telephone')[0].text_content())
	address = str(row.cssselect('div.businessCapsule--address')[0].text_content())
		       
		    
	teamItem = {
	'id':id,
	'name':name,
	'telephone':telephone,
	'address':address
	}
		    
	premierLeagueData.append(teamItem)
		
	if len(premierLeagueData) > 0:
		#truncate data store
		scraperwiki.sql.execute("DROP TABLE IF EXISTS `data`")
		#add each table line to data store
	for teamItem in premierLeagueData:
		scraperwiki.sql.save(['id'], teamItem)


