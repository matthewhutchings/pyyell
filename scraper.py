#!/usr/bin/env python
import requests
import lxml.html
import scraperwiki


locations = "poole", "bournemouth", "swanage" , "wareham"
for search_location in locations:

	query = "electrician", "solar", "gym"
	for search in query:
	
		train = "1", "2", "3", "4","5","6","7","8","9"
		for name in train:
		
			url = 'http://www.yell.com/ucs/UcsSearchAction.do?keywords='+search+'&location='+search_location+'&scrambleSeed=833794509&pageNum='+name  
		 
		 	print url
		
		 	html = requests.get(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36"}).content
			dom = lxml.html.fromstring(html)
			premierLeagueData = []
			
			x = 1
							
			for row in dom.cssselect('div.businessCapsule-fle'):
				x += 1
				
				print x
					    
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
				
				print teamItem
				
				print "test"


if len(premierLeagueData) > 0:
	#truncate data store
	scraperwiki.sql.execute("DROP TABLE IF EXISTS `data`")
	#add each table line to data store
for teamItem in premierLeagueData:
	scraperwiki.sql.save(['id'], teamItem)


	
