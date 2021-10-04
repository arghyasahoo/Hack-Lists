# Scraping web for hackathons and listing them

from bs4 import BeautifulSoup as bs
import requests as r
from datetime import date as dt


def collectData():
    url = "https://mlh.io/seasons/2021/events"

    today = (dt.today()).strftime("%Y-%m-%d")

    source = r.get(url).text

    soup = bs(source, 'lxml')

    event_names = soup.find_all('h3', class_='event-name')
    event_links = soup.find_all('a', class_='event-link', href=True)
    event_startdate = soup.find_all('meta', itemprop='startDate')
    event_enddate = soup.find_all('meta', itemprop='endDate')

    number_of_events = len(event_names)

    status = None

    for i in range(number_of_events):

        if (today < event_startdate[i]['content']):
            with open("../tmp/upcoming/mlh.txt", 'a') as hl:
                status = "Upcoming"
                data = event_names[i].text + ' :: ' + 'Major League Hacking' + ' :: ' + event_startdate[i]['content'] + \
                    ' :: ' + event_enddate[i]['content'] + \
                    ' :: ' + status + ' :: ' + event_links[i]['href']
                hl.write(data + '\n')

        elif (today >= event_startdate[i]['content'] and today <= event_enddate[i]['content']):
            with open("../tmp/ongoing/mlh.txt", 'a') as hl:
                status = "Ongoing"
                data = event_names[i].text + ' :: ' + 'Major League Hacking' + ' :: ' + event_startdate[i]['content'] + \
                    ' :: ' + event_enddate[i]['content'] + \
                    ' :: ' + status + ' :: ' + event_links[i]['href']
                hl.write(data + '\n')

        else:
            with open("../tmp/past/mlh.txt", 'a') as hl:
                status = "Past"
                data = event_names[i].text + ' :: ' + 'Major League Hacking' + ' :: ' + event_startdate[i]['content'] + \
                    ' :: ' + event_enddate[i]['content'] + \
                    ' :: ' + status + ' :: ' + event_links[i]['href']
                hl.write(data + '\n')


collectData()
