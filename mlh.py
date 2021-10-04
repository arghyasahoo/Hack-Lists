# Scraping web for hackathons and listing them

from bs4 import BeautifulSoup as bs
import requests as r
from datetime import date as dt

def collectData():
	url = "https://mlh.io/seasons/2021/events"

	today = (dt.today()).strftime("%Y-%m-%d")
	print(today)

	source = r.get(url).text

	soup = bs(source, 'lxml')

	events = soup.find_all('div', class_='container feature')

	event_names = soup.find_all('h3', class_='event-name')
	event_links = soup.find_all('a', class_='event-link', href=True)
	event_dates = soup.find_all('p', class_='event-date')
	event_startdate = soup.find_all('meta', itemprop='startDate')
	event_enddate = soup.find_all('meta', itemprop='endDate')

	number_of_events = len(event_names)

	status = None

	with open("hackathonList.txt", 'w') as hl:
		for i in range(number_of_events):
			if (today < event_startdate[i]['content']):
				status = "Upcoming"
			elif (today >= event_startdate[i]['content'] and today <= event_enddate[i]['content']):
				status = "Ongoing"

			# print(type(event_names[i].text))
			# print(type(event_startdate[i]['content']))
			# print(type(event_enddate[i]['content']))
			# print(type(event_links[i]['href']))

			data = event_names[i].text + ' :: ' + 'Major League Hacking' + ' :: ' + event_startdate[i]['content'] + ' :: ' + event_enddate[i]['content'] + ' :: ' + ' :: ' + event_links[i]['href']
			
			hl.write(data + '\n')


def getStats():
	import PythonProfiler
	
	p = PythonProfiler.Profile(True)
	p.profile(["collectData()"])

getStats()