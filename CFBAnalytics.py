import requests
from lxml import html
import pandas as pd


# Function to populate elemnts with xpath
def elements(page_xpath):
    return tree.xpath(page_xpath)


# function to find team with the given Points For (PF) and Points Against(PA)
def getTeamsPFPA(team_pf, team_pa):
    teams_pf = []
    teams_pa = []
    for teams, l_team_stats in team_stats.items():
        if l_team_stats[4] == team_pf:
            teams_pf.append(teams)
        if l_team_stats[5] == team_pa:
            teams_pa.append(teams)
    return teams_pf, teams_pa


# Using requests and BeautifulSoup to retrieve html info from website
page = requests.get('https://www.ncaa.com/standings/football/fbs')
tree = html.fromstring(page.content)

# The differnect xpaths used to retrieve the info
conf_xpath = '//figure[@class="standings-conference"]/text()'
div_xpath = '//th[@class="school-col"]/text()'
stat_xpath = '//td/text()'

# Uses the 'elemnts' function from above
conferences = elements(conf_xpath)
divisions = elements(div_xpath)
divisions2 = []
stats = list(elements(stat_xpath))

# When creating the divisions elemetns, 'School' was included but needs to be removed
invalid = 'School'
for division in divisions:
    if division != invalid:
        divisions2.append(division)

# Populating all the stats from the stats elements
teams, con_wins, con_losses, wins, losses, pf, pa, home, away, streak = [], [], [], [], [], [], [], [], [], []
sta = [teams, con_wins, con_losses, wins, losses, pf, pa, home, away, streak]
for i in range(len(sta)):
    sta[i] = stats[i::10]

# Changing type of certain values to int for comparison
for item in range(1, len(sta) - 3):
    sta[item] = [int(each_item) for each_item in sta[item]]

item = 0
for item in range(len(sta) - 3, len(sta)):
    sta[item] = [str(each_item) for each_item in sta[item]]
teams, con_wins, con_losses, wins, losses, pf, pa, home, away, streak = sta[0], sta[1], sta[2], sta[3], sta[4], sta[5], sta[6], sta[7], sta[8], sta[9]

# Making each team in teams uppercase for comparing to user input
teams = [team.upper() for team in teams]

# Zipping all the stats into one list
l_team_stats = list(zip(con_wins, con_losses, wins, losses, pf, pa, home, away, streak))

# Assigning stat values to each team in a dictionary
team_stats = {}
i = 0
for i in range(0, len(teams)):
    team_stats[teams[i]] = l_team_stats[i]

# Requesting response from user to enter FBS team name
# For given team, all stats are displayed
i = 0
list_stats = ['Conference Wins: ', 'Conference Losses: ', 'Total Wins: ', 'Total Losses: ', 'Points For: ', 'Points Against: ', 'Home: ', 'Away: ', 'Streak: ']

resp = input('Enter a team to find their stats: ')

if resp.upper() in teams:
    for i in range(len(list_stats)):
        print(list_stats[i], team_stats[resp.upper()][i])
else:
    print('Team could not be found')
print('')

# Finding maxes and mins for pa and pf
maximum_pa = max(pa)
minimum_pa = min(pa)
maximum_pf = max(pf)
minimum_pf = min(pf)

# Uses the 'getTeamsPFPA' fucntion for pa and pf from above
minPFPA = getTeamsPFPA(minimum_pf, minimum_pa)
maxPFPA = getTeamsPFPA(maximum_pf, maximum_pa)

print('Team(s) with the lowest Points Against: ', minPFPA[1])
print('Team(s) with the highest Points Against: ', maxPFPA[1])
print('Team(s) with the lowest Points For: ', minPFPA[0])
print('Team(s) with the highest Points For: ', maxPFPA[0])

pd.DataFrame({'Team': teams, 'Conference Wins': con_wins, 'Conference Losses': con_losses, 'Wins': wins, 'Losses': losses, 'Points For': pf, 'Points Against': pa, 'Streak': streak}).to_csv('CFBAnalytics.csv', index=False)
# for team_stat in team_stats:
#     print(team_stat, team_stats[team_stat])
