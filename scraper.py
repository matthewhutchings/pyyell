#!/usr/bin/env python
import requests
import lxml.html
import scraperwiki

 scraperwiki.sql.execute("DROP TABLE IF EXISTS `data`")

html = requests.get('https://www.yell.com/ucs/UcsSearchAction.do?keywords=pizza&location=southampton&scrambleSeed=833794509').content

dom = lxml.html.fromstring(html)

premierLeagueData = []

for row in dom.cssselect('div.businessCapsule-fle'):
    
    
    
    pos = int(row.cssselect('div.col-sm-24')[0].text_content())
    
    
       
    
    teamItem = {'pos':pos}
    
    premierLeagueData.append(teamItem)

if len(premierLeagueData) > 0:
    #truncate data store
    scraperwiki.sql.execute("DROP TABLE IF EXISTS `swdata`")
    #add each table line to data store
    for teamItem in premierLeagueData:
        scraperwiki.sql.save(['team'], teamItem)



