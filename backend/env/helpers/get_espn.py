import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os.path import exists
from pathlib import Path
from csv import reader, writer
from itertools import combinations
from operator import itemgetter

def get_espn():
    today = date.today().strftime("%d/%m/%Y")
    today = today.replace('/', '_')
    base_path = Path(__file__).parent
    file_path = (base_path / f"../espn_csv/espn_{today}.csv")
    file_exists = exists(file_path)
    if file_exists:
        print('file exists')
        with open(file_path, 'r') as read:
            return list(reader(read))                

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get('https://fantasy.espn.com/football/players/projections')

    driver.implicitly_wait(5)

    pages = driver.find_elements(By.CLASS_NAME, 'Pagination__list__item__link')
    page_count = int(pages[-1].text) - 1

    espn_projections = []
    # try:
    for i in range(page_count):
        players = driver.find_elements(By.CLASS_NAME, "player-info-section")
        with open(file_path, 'a', newline='') as csvfile:
            csvwriter = writer(csvfile)
            for player_ in players:
                stats = player_.find_elements(By.TAG_NAME, 'table')
                player = stats[0]
                stats = stats[1]
                player = player.find_element(By.TAG_NAME, 'a').text
                projection = stats.find_elements(By.TAG_NAME, 'tr')[-1 ].find_elements(By.TAG_NAME, 'td')[-1].text
                if projection == '--':
                    projection = 0
                # if float(projection) < 5:
                #     continue
                espn_projections.append([player, projection])
                csvwriter.writerow([player, projection])

            button = driver.find_element(By.CLASS_NAME, 'Pagination__Button--next')
            button.click()
            time.sleep(2)
    # except:
    #     print('espn scrap failed')
    #     driver.quit()
    return espn_projections