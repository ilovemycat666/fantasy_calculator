import time
import json 
from csv import reader
from itertools import combinations
from operator import itemgetter

from helpers.get_espn import get_espn
from helpers.make_roster import make_roster, parse_injuries, short_roster_by_value
from helpers.picks import picks
from helpers.quick_combinations import quick_combinations

from flask import Flask, request

"""
Use python virtual env to run 
cd to backend folder
For windows users: 
> .\env\Scripts\activate
For mac/unix users: 
> source env/bin/activate

to start:
cd to env
> flask run

To close: 
> deactivate
"""

app = Flask(__name__)

@app.route('/createTeams', methods = ['POST'])
def my_profile():
    start = time.time()
    one = set(['ed', 'cate'])
    two = set(['cate', 'ed'])
    print("&^&^&^&^&^&^&^&^&^^&")
    print(one == two)
    print("&^&^&^&^&^&^&^&^&^^&")

# receive input from React
# - form['fanduelCsv'] is the user submited csv defining their betting pool
# - form['playerPicks'] are the users locked players
    form = request.form
    player_picks = form['playerPicks']
    fanduel_csv = request.form['fanduelCsv']
    fanduel_csv = json.loads(fanduel_csv)[0]
    fanduel_csv = [i.split(',') for i in fanduel_csv]
# Triggers a helper to scrap for ESPN data, or return the csv if it already exists
    espn_projections = get_espn()
# Uses user CSV to determine eligibile players + adds in ESPN projections
    roster = make_roster(fanduel_csv, espn_projections)
    print("len fandule", len(fanduel_csv))
    print("len espn", len(espn_projections))
    print("len roster", len(roster))
# removes injured players, creates positions list for short roster
    full_roster, positions_lists = parse_injuries(roster)
# locks in user picks 
    player_picks, bad_pick = picks(full_roster, player_picks)
    if len(bad_pick) != 0:
        return bad_pick
# shortens roster per position by given step count
# only uses as many players per position as listed
# using whole roster takes too long
    shorter_roster_by_position = short_roster_by_value(6, player_picks, positions_lists)
# creates all combinations of players
# 2 params
# - list - all players
# - int - length of each group of combinations 
    # league = list(combinations(shorter_roster_by_position, (9 - len(player_picks))))
    teams = sorted(quick_combinations(shorter_roster_by_position, player_picks), key=itemgetter(0), reverse=True)

    fewer_teams = teams[:500]

    display_teams = []
    list_names = []
    for team in fewer_teams:
        names = set([i[2] for i in team[2]])
        if names in list_names:
            continue
        else:
            list_names.append(names)
            display_teams.append(team)


# filters outcome from combinations for eligible teams
# sorts based on team projected points 
    # teams = sorted(make_fanduel_team(league, player_picks), key=itemgetter(0), reverse=True)

    # response_body = {
    #     "teams": teams
    # }

# returns top 20
    print(f'{time.time() - start} Seconds')
    if len(teams) == 0:
        return ["No teams fit your parameters"]
    return display_teams[:20]
