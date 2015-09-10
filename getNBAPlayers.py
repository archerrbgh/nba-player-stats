import requests
from bs4 import BeautifulSoup

teams = {"Celtics":'bos',"Nets":'bkn',"Knicks":'nyk',"76ers":'phi',"Raptors":'tor',"Warriors":'gsw','Clippers':'lac',"Lakers":'lal',"Suns":'pho',"Kings":'sac',"Bulls":'chi',"Cavaliers":'cle',"Pistons":'det',"Pacers":'ind',"Bucks":'mil',"Mavericks":'dal',"Rockets":'hou',"Grizzlies":'mem',"Pelicans":'nor',"Spurs":'sas',"Hawks":'atl',"Hornets":'cha',"Heat":'mia',"Magic":'orl',"Wizards":'was',"Nuggets":'den',"Timberwolves":'min',"Thunder":'okc',"Blazers":'por',"Jazz":'uth'}

url = 'http://espn.go.com/nba/teams/roster?team='

outfile = open('NBAPlayers.txt','w')

for team in teams.values():
	print url+team
	outfile.write(team + '\n')
	r = requests.get(url+team)
	soup = BeautifulSoup(r.text,'lxml')
	players = soup.find_all('td', class_ = 'sortcell')
	for player in players:
		info = player.a
		outfile.write(info.text + ' ' + info['href'] + '\n')

outfile.close()