import requests
import pandas as pd
from bs4 import BeautifulSoup
schedule_url = "https://www.basketball-reference.com/leagues/NBA_2025_totals.html"
r = requests.get(schedule_url)
soup = BeautifulSoup(r.content, 'html5lib')

def player_pos_extracts():
    data_stats = ["name_display", "pos"]
    results = {}
    for stat in data_stats:
        elements = soup.find_all(attrs={"data-stat": stat})
        # Check if there is an <a> tag and get the text accordingly
        results[stat] = [
            element.a.text if element.a else element.text for element in elements
        ]

    # player_position = soup.find('tbody').find_all('td', {'data-stat': 'pos'})
    # player_name = soup.find('tbody').find_all('a')
    df = pd.DataFrame(results)[1:] #starting from the first index as it adds header into the dataframe as the first row
    df.columns = ['PLAYER_NAME', 'Position']
    df.to_csv('player_positions.csv')
    return df