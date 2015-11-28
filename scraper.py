#!/usr/bin/env python
import requests
import lxml.html
import scraperwiki

html = requests.get('https://www.yell.com/ucs/UcsSearchAction.do?keywords=pizza&location=southampton&scrambleSeed=833794509', headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36"}).content

dom = lxml.html.fromstring(html)

premierLeagueData = []

x = 1

for row in dom.cssselect('div.businessCapsule-fle'):
    
    x += 1
    
    team = x
    pos = string(row.cssselect('div.col-sm-24')[0].text_content())
    
    
       
    
    teamItem = {'pos':pos, 'team':team}
    
    premierLeagueData.append(teamItem)

if len(premierLeagueData) > 0:
    #truncate data store
    scraperwiki.sql.execute("DROP TABLE IF EXISTS `swdata`")
    #add each table line to data store
    for teamItem in premierLeagueData:
        scraperwiki.sql.save(['team'], teamItem)


