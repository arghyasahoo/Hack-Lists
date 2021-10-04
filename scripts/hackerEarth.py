import requests,re
from datetime import datetime
from bs4 import BeautifulSoup

date=datetime.now()

url="https://www.hackerearth.com/challenges/hackathon/"
page_data=requests.get(url)
soup_data=BeautifulSoup(page_data.content,'html.parser')
result_data=soup_data.find(id="challenge-container")
all_ongoing_contest=result_data.find_all(class_='challenge-card-modern')
hackathon_dets=[]
for i in all_ongoing_contest:
    contest_organizer_name=''
    contest_name_str=i.find(class_="challenge-name ellipsis dark").find("span")
    contest_name=re.findall(">([a-zA-Z]\S*.+)<",str(i))
    contest_link=i.find('a',class_="challenge-card-wrapper challenge-card-link")
    con_link=contest_link.get('href')
    contest_organiser=i.find(class_="company-details ellipsis")
    if contest_organiser is not None:
        contest_organizer_name=contest_organiser.get_text()
    hackathon_data=BeautifulSoup(requests.get(contest_link.get('href')).content,'html.parser')
    steps_hackathon=hackathon_data.find('div',class_="event-details-container").findChildren('div',recursive=False)
    times=re.findall("([A-Z]{1}[a-z]{1}[a-z]{1}\s[\d]{1,2}[,]\s[\d]{4}[,]\s[\d]{1,2}[:][\d]{1,2}\s[A-Z]{1,2})",str(steps_hackathon))
    start_end=re.findall(">([a-z]{3,6}\son:)<",str(steps_hackathon))
    # print(contest_name," ",con_link," ",contest_organizer_name," ",(times,start_end),end="\n\n")
    # print(contest_organizer_name)
    hackathon_dets.append([contest_name,con_link,contest_organizer_name,times,start_end])

with open("./tmp/upcoming/hackerEarth.txt","w") as wr:
    for hack in hackathon_dets:
        hack_org_name=re.sub('[\W_\n<>]+','',str(hack[2]))
        start_time=datetime.strptime(str(hack[3][0]),"%b %d, %Y, %I:%M %p")
        end_time=datetime.strptime(str(hack[3][len(hack[3])-1]),"%b %d, %Y, %I:%M %p")
        time='starts_on: '+str(start_time)+' :: '+' ends_on: '+str(end_time )
        if date < start_time:
            data = hack[0][0]+' :: '+hack_org_name+' :: '+time+' :: '+'Upcoming'+' :: '+str(hack[1])
            wr.write(data+'\n')
wr.close()
with open("./tmp/ongoing/hackerEarth.txt","w") as wr1:
    for hack in hackathon_dets:
        hack_org_name=re.sub('[\W_\n<>]+','',str(hack[2]))
        start_time=datetime.strptime(str(hack[3][0]),"%b %d, %Y, %I:%M %p")
        end_time=datetime.strptime(str(hack[3][len(hack[3])-1]),"%b %d, %Y, %I:%M %p")
        time='starts_on: '+str(start_time)+' :: '+' ends_on: '+str(end_time )
        if date >= start_time:
            # print(str(hack[3]).split(','))
            # print(datetime.strptime(str(hack[3][0]),"%b %d, %Y, %I:%M %p"))
            data = hack[0][0]+' :: '+hack_org_name+' :: '+time+' :: '+'Ongoing'+' :: '+str(hack[1])
            wr1.write(data+'\n')
wr1.close()






