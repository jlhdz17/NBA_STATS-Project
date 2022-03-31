from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()




def get_links():
  data = get(BASE_URL + ALL_JSON).json()
  links = data['links']
  return links


def get_scoreboard():
  scoreboard = get_links()['currentScoreboard']
  games = get(BASE_URL + scoreboard).json()['games']

  for game in games:
    home_team = game['hTeam']
    away_team = game['vTeam']
    clock = game['clock']
    period = game['period']
    
    print("-----------------------------------------------------")
    print(f"{home_team['triCode']} vs {away_team['triCode']}")
    print(f"{home_team['score']} - {away_team['score']}")
    print(f"{clock} - {period['current']}")



def get_stats():
  stats = get_links()['leagueTeamStatsLeaders']
  teams = get(BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']
  

  teams = list(filter(lambda x: x['name'] != "Team", teams))
  teams.sort(key=lambda x: int(x['ppg']['rank']))

  
  for i, team in enumerate(teams):
    name = team['name']
    nickname = team['nickname']
    ppg = team['ppg']['avg']
    print(f"{i+1}. {name} - {nickname} - {ppg}")

  printer.pprint(teams[0].keys())

def get_ecstandings():
    ecteams = get_links()['leagueConfStandings']
    east = get(BASE_URL + ecteams).json()['league']['standard']['conference']['east']

    for ceast in east:
        teamId = ceast['teamId']
        win = ceast['win']
        loss = ceast['loss']
        print(f"{teamId} - {win} - {loss}")

def get_wcstandings():
    wcteams = get_links()['leagueConfStandings']
    west = get(BASE_URL + wcteams).json()['league']['standard']['conference']['west']


    for cwest in west:
        teamId = cwest['teamId']
        win = cwest['win']
        loss = cwest['loss']
        print(f"{teamId} - {win} - {loss}")




ans = input("Welcome to the NBA Data Center! Please type if you want Scoreboard, Stats, ECStandings, WCStandings: " )

if ans == "Scoreboard" or "scoreboard":
    print(get_scoreboard())
elif ans == "Stats" or "stats":
    print(get_stats())
elif ans == "ECStandings" or "ECstandings":
    print(get_ecstandings())
elif ans == "WCStandings" or "WCstandings":
    print(get_wcstandings())
else:
    print("Sorry I didn't read that, please try again!")





    




