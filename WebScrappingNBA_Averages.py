from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# the year
year = input("Enter the year: ")

## url of the page
url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)

html = urlopen(url)

soup = BeautifulSoup(html, features="html.parser")

# get column headers
soup.findAll('tr', limit=2)

# create a list of the headers
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

headers = headers[1:]

rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]

stats = pd.DataFrame(player_stats, columns = headers)

stats_clean = stats.dropna()
print(stats_clean)

stats_clean.to_csv('nba_stats_{}.csv'.format(year))
