import requests,re
from datetime import datetime
from bs4 import BeautifulSoup


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

with open("hackathonList1.txt","w") as wr:
    for hack in hackathon_dets:
        hack_org_name=re.sub('[\W_\n<>]+','',str(hack[2]))
        start_time=datetime.strptime(str(hack[3][0]),"%b %d, %Y, %I:%M %p")
        end_time=datetime.strptime(str(hack[3][len(hack[3])-1]),"%b %d, %Y, %I:%M %p")
        time='starts_on: '+str(start_time)+' :: '+' ends_on: '+str(end_time )
        # print(str(hack[3]).split(','))
        # print(datetime.strptime(str(hack[3][0]),"%b %d, %Y, %I:%M %p"))
        data = hack[0][0]+' :: '+hack_org_name+' :: '+time+' :: '+str(hack[1])
        wr.write(data+'\n')

    












# contest name---
# contest organizer----
# contest start and ends date----xxxxxxxx
# contest link---
# technologies used by contest


# contest_link=all_ongoing_contest[0].find('a',class_="challenge-card-wrapper challenge-card-link").get('href')
# hackathon_data=BeautifulSoup(requests.get(contest_link).content,'html.parser')
# steps_hackathon=hackathon_data.find('div',class_="event-details-container").findChildren('div',recursive=False)
# start_end=re.findall(">([a-z]{3,6}\son:)<",str(steps_hackathon))
# print(start_end)
# all_links=[]
# all_links.append(contest_link.get('href'))
# print(all_links)
# contest_name_str=all_ongoing_contest[0].find(class_="challenge-name ellipsis dark").find("span")
# contest_name=re.findall('>([a-zA-Z]\S*.+)<',str(contest_name_str))
# print(contest_name,end='\n')
# contest_link=all_ongoing_contest[0].find('a',class_="challenge-card-wrapper challenge-card-link").get('href')
# starting_date=hackathon_data.find(class_="start-time-block").get_text()
# ending_date=hackathon_data.find(class_="end-time-block").get_text()
# print(times)
# print(result_data.prettify())