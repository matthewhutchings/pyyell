#!/usr/bin/env python
import requests
import lxml.html
import scraperwiki
import options



locations = "poole", "bournemouth", "swanage" , "wareham"
for search_location in locations:

	query = options.business_options
	for search in query:
	
		train = "1", "2", "3", "4","5","6","7","8","9"
		for name in train:
		
			url = 'http://www.yell.com/ucs/UcsSearchAction.do?keywords='+search+'&location='+search_location+'&scrambleSeed=833794509&pageNum='+name  
		 

		 	html = requests.get(url, headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:42.0) Gecko/20100101 Firefox/42.0"}).content
			dom = lxml.html.fromstring(html)
			premierLeagueData = []
			
			print "Searching for '"+search+"' in "+search_location+" Page:"+name

			x = 1
							
			for row in dom.cssselect('div.businessCapsule-fle'):
				x += 1
				
				print "Found: "+x
					    
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
				
			else:
			 print html
			 quit()


if len(premierLeagueData) > 0:
	#truncate data store
	scraperwiki.sql.execute("DROP TABLE IF EXISTS `data`")
	#add each table line to data store
for teamItem in premierLeagueData:
	scraperwiki.sql.save(['id'], teamItem)


	
