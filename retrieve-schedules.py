# Author: Evan Pesch
# Filename: retrieve-schedules.py
# Last Updated: November 29, 2019


import urllib.request
import csv
from bs4 import BeautifulSoup
import pandas as pd


def getTeams ():
	page = urllib.request.urlopen('https://www.mlb.com/angels/fans/downloadable-schedule')
	soup = BeautifulSoup(page,  "html.parser")
	teamNames = []
	for div  in soup.findAll('div', attrs={'class': "header__subnav--teams__teams"}):
		for anchor in div.findAll('a', href=True):
			teamNames.append(anchor['href'][1:])
	return teamNames

teamNamesArray = getTeams()


for team in teamNamesArray:
	page = urllib.request.urlopen('https://www.mlb.com/' + team + '/fans/downloadable-schedule')
	soup = BeautifulSoup(page,  "html.parser")
	# for h1 in soup.findAll('h1', attrs={'class': "p-page-banner__title"}):
	divArray = []
	for div in soup.findAll('div', attrs={'class': "p-wysiwyg"}):
		divArray.append(div)
	myDiv = divArray[2]

	# Find needed li tags
	liArray = []
	for li in myDiv.findAll('li'):
		liArray.append(li)
	myLi = liArray[1]

	# Find needed a tag
	myA = myLi.find('a',  href=True)

	# Find needed href from a tag and replace needed string in url. Could this be done without needing to replace text?
	myScheduleLink = myA['href']
	myScheduleLink = myScheduleLink.replace('mlb.mlb.com', 'www.ticketing-client.com')
	# print(myScheduleLink)

	# Read data as CSV
	data = pd.read_csv(myScheduleLink)
	x = data.head()
	# print(x)

	# Save csv to file in schedules directory
	data.to_csv('schedules/' + team + '-home-schedule.csv')
