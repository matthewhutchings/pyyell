#!/usr/bin/env python
import requests
import lxml.html
import scraperwiki

html = requests.get('https://www.yell.com/ucs/UcsSearchAction.do?keywords=pizza&location=southampton&scrambleSeed=833794509').content

dom = lxml.html.fromstring(html)

premierLeagueData = []

for row in dom.cssselect('div.businessCapsule-fle'):
    
    
    
    pos = int(row.cssselect('div.col-sm-24')[0].text_content())
    
    
    
    team = row.cssselect('.col-club')[0].text_content()
    goalsFor = int(row.cssselect('.col-gf')[0].text_content())
    goalsAgainst = int(row.cssselect('.col-ga')[0].text_content())
    goalDifference = int(row.cssselect('.col-gd')[0].text_content())
    points = int(row.cssselect('.col-pts')[0].text_content())
    
    print pos, team,"gf", goalsFor, "ga", goalsAgainst, "gd", goalDifference, "pts", points
    
    
    teamItem = {'pos':pos,
        'team':team,
        'gf':goalsFor,
        'ga':goalsAgainst,
        'gd':goalDifference,
        'pts':points}
    premierLeagueData.append(teamItem)

if len(premierLeagueData) > 0:
    #truncate data store
    scraperwiki.sql.execute("DROP TABLE IF EXISTS `swdata`")
    #add each table line to data store
    for teamItem in premierLeagueData:
        scraperwiki.sql.save(['team'], teamItem)



