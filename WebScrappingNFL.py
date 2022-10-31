from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# selecting the year and category
year = input("Enter the year: ")
cat = input("Passing, Rushing, or Receiving: ")


## url of the page
url = 'https://www.pro-football-reference.com/years/{}/{}.htm'.format(year,cat.lower())

html = urlopen(url)

soup = BeautifulSoup(html, features="html.parser")

# get column headers
soup.findAll('tr', limit=2)

# create a list of the headers
if cat == "Rushing":
    headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
    headers = headers[1:]
    rows = soup.findAll('tr')[2:]
else:
    headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
    headers = headers[1:]
    rows = soup.findAll('tr')[1:]

#creates a 2d list of the players stats
player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]

#turn the list into a dataframe
stats = pd.DataFrame(player_stats, columns = headers)

#removes unfit players
stats_clean = stats.dropna()

print(stats_clean)
stats_clean.to_csv('nfl_stats_{}_{}.csv'.format(year,cat.lower()))
