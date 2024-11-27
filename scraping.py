from bs4 import BeautifulSoup
import pandas as pd
import requests
import cloudscraper
import re

url = 'https://www.365scores.com/es/football/team/fc-barcelona-132'
# url = 'https://es.whoscored.com/Teams/65/Show/Espa%C3%B1a-Barcelona'


# Adding Browser / User-Agent Filtering should help ie. 

# will give you only desktop firefox User-Agents on Windows
# scraper = cloudscraper.create_scraper(browser={'browser': 'chrome','platform': 'windows','mobile': False})
# html = scraper.get(url).content
# soup = BeautifulSoup(html, 'html.parser')

# BASIC SETTINGS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# driver.set_window_size(200,200)
driver.maximize_window()
driver.get(url)
driver.find_element(By.XPATH, "//div[normalize-space()='Resultados']").click()
time.sleep(5)

html = driver.page_source
# driver.quit()
soup = BeautifulSoup(html, 'html.parser')

table = soup.find('div', {'class': 'entity-scores-widget_container__3l7E3 entity-scores-widget_side_bar__qDDmx'})
matches = table.find_all('a', {'class': 'game-card_game_card_link__L3moj game-card_game_card__RpinR game-card_clickable__-fXXf game-card_support_hover__ES-mS link_link__Zkmqt'})

# for match in matches:
#     if len(match) == 7:
#         team1, img1, status, result, img2, team2, bet = match.contents
#     if len(match) == 8:
#         team1, img1, status, result, img2, team2, cards, bet = match.contents
#     print(team1.text, result.text, team2.text)

local_teams, visiting_teams, results = [], [], []

for match2 in matches:
    teams = match2.find_all('div', {'class': 'ellipsis_container__ciMmU'})
    score = match2.find('div', {'class': 'game-card-center_center_score__UjTgF game-score_container__47pDv'})
    team1, team2 = teams
    print(team1.text, score.text, team2.text)
    local_teams.append(team1.text)
    visiting_teams.append(team2.text)
    results.append(score.text)

df = pd.DataFrame({'Local Team': local_teams, 'Visiting Team': visiting_teams, 'Result': results})

df.to_csv('matches.csv', index = False)