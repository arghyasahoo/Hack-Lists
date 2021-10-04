import requests
from bs4 import BeautifulSoup as soup
import datetime as dt

def getDate(date):
    month = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06", "july": "07", "august": "08", "september": "09", "october": "10", "november": "11", "december": "12"}
    ls = date.lower().split()
    m = month[ls[0]]
    staring, ending = '0', '0'
    try:
        staring, ending = ls[1].split("–")
    except:
        staring = ls[1]

    x = dt.datetime.now()
    try:
        staring_date = dt.date(x.year, int(m), int(staring))
    except:
        staring_date = "-"
    
    try:
        ending_date = dt.date(x.year, int(m), int(ending))
    except:
        ending_date = "-"

    return (staring_date, ending_date)


url = "https://hackathons.hackclub.com/"
rq = requests.get(url)
container = soup(rq.text, 'lxml')
names = container.select(".css-mu5syq")
dates = container.select(".css-vurnku")
links = container.find_all("a", "css-1bn5qip")
nameList = []
dateList = []
linkList = []
for x in names:
    nameList.append(x.getText())

i = 0
while i < (len(dates)):
    dateList.append(dates[i].getText())
    i += 2

for x in links:
    linkList.append(x.get("href"))

with open("./tmp/ongoing/1.txt","w") as wr:
    for i in range(len(nameList)):
        starting, ending = map(str, getDate(dateList[i]))
        wr.write(nameList[i] + " :: " + nameList[i] + " :: " + starting + " :: " + ending + " :: Ongoing :: " + linkList[i]+ "\n")