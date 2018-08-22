from datetime import datetime
from dateutil.parser import parse
from lxml import html
import requests
import math

def getAge(birthday, date=datetime.today()):
    age = date.year - birthday.year
    if date < datetime(date.year, birthday.month, birthday.day):
        age -= 1

    return age


def avgTime(RecvDateClean,OffenseDateClean):
    DiffTime = RecvDate - OffenseDate
    intDiffTime = int(DiffTime)
    AvgDiffTime = intDiffTime / 231
    return AvgDiffTime


    
url = "https://www.tdcj.state.tx.us/death_row/dr_offenders_on_dr.html"

doc = html.fromstring(
    requests.get(
        url
    ).text
)

# Our rows look like this:
# [ID, Link, LastName, FirstName, Birthdate, Sex, Race, RecvDate, County, OffenseDate]

inmateTable = doc.xpath('//table/tr')[1:]

#print("There are currently {} inmates on death row in Texas.".format(len(inmateTable)))

bdayMax = 0

date1 = []
date2 = []

for i in inmateTable:
    RecvDate = i.cssselect('td')[7].text_content()
    RecvDateClean = parse(RecvDate)
    date1.append(RecvDateClean)
    OffenseDate = i.cssselect('td')[9].text_content()
    OffenseDateClean = parse(OffenseDate)
    date2.append(OffenseDateClean)

diffyears = []
for d in date2:
    for x in date1:
        diffyears.append((x - d).day:


for i in diffyears:
    diffyears = list(map(int, diffyears))
    sum += cat

print(int(cat))

#avgTime(RecvDateClean,OffenseDateClean)
