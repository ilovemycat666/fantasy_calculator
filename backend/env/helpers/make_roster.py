from operator import itemgetter


# fan player
#     0           1      2            3             4               5              6     7         8        9      10
# ['81803-8803', 'QB', 'Chase', 'Chase Daniel', 'Daniel', '-0.20000000298023224', '1', '5000', 'DEN@LAC', 'LAC', 'DEN', '', '', '', '', '', 'MVP - 1.5X Points/AnyFLEX']


# def make_roster(fanduel_roster, espn_projections):
#     rejects = set()
#     roster = []
#     for fan_player in fanduel_roster:
#         print("fan player", fan_player)
#         if fan_player[3] == 'Josh Johnson' and fan_player[1] == 'RB':
#             continue
#         for espn_player in espn_projections:
#             # account for defensive team naming convention
#             if fan_player[3] == espn_player[0] or fan_player[1] == 'D' and fan_player[4] == espn_player[0].split()[0]:
#                 value = ((float(espn_player[1])/ float(fan_player[7])) * 1000)
#                 value = float("{:.2f}".format(value))
#                 #        ID 0, position 1, full name 2, salary 3, espn projection 4, value rating 5, injury 6, Team 8, Game 9
#                 slip = [fan_player[0], fan_player[1], fan_player[3], fan_player[7], espn_player[1], value, fan_player[11], fan_player[8], fan_player[9]]
#                 roster.append(slip)
#             else:
#                 rejects.add(fan_player[3])
#                 print(fan_player)
#     for reject in rejects:
#         print(reject)
#     return roster

def make_roster(fanduel_roster, espn_projections):
    roster = []
    espn_names = [i[0] for i in espn_projections]
    for fan_player in fanduel_roster:
        if fan_player[1] != 'D':
            if fan_player[3] in espn_names:
                espn_name_index = espn_names.index(fan_player[3])
                fppg = espn_projections[espn_name_index][1]
                if fan_player[3] == "Justin Herbert":
                    print(fan_player)
                elif fan_player[3] == "Joe Burrow":
                    print(fan_player)
        # handles differences in defence naming
        elif fan_player[1] == 'D':
            if fan_player[3].split(" ")[-1] in espn_names:
                espn_name_index = espn_names.index(fan_player[3].split(" ")[-1])
                fppg = espn_projections[espn_name_index][1]
                # print("the Ds: ", fan_player)
        value = ((float(fppg))/float(fan_player[7]) * 1000)
        value = float("{:.2f}".format(value))
        slip = [fan_player[0], fan_player[1], fan_player[3], fan_player[7], fppg, value, fan_player[11], fan_player[8], fan_player[9]]
        roster.append(slip)
    return roster


def parse_injuries(roster):
    QB = []
    RB = []
    WR = []
    TE = []
    D = []
    full_roster = []
    for player in roster:
        if player[6] in ['IR', 'NA', 'O', 'D', 'P', 'Q']:
            continue
        # split team by position
        if player[1] == "QB":
            QB.append(player[:6] + player[7:])
        elif player[1] == "RB":
            RB.append(player[:6] + player[7:])
        elif player[1] == "WR":
            WR.append(player[:6] + player[7:])
        elif player[1] == "TE":
            TE.append(player[:6] + player[7:])
        elif player[1] == "D":
            D.append(player[:6] + player[7:])
        full_roster.append(player[:6] + player[7:])
    print(len(QB))
    print(len(RB))
    print(len(WR))
    print(len(TE))
    print(len(D))
    positions_lists = [QB, RB, WR, TE, D]
    return full_roster, positions_lists


# def short_roster_by_value(increment, player_picks, positions_list):
#     step = increment + len(player_picks)
#     print(f"Step setting: {step}")
#     short_roster = []
#     for i in positions_list:
#         # order positions by value
#         i = sorted(i, key=itemgetter(5), reverse=True)[:step]
#         short_roster.extend(i)
#     return short_roster


def short_roster_by_value(increment, player_picks, positions_list):
    step = increment + len(player_picks)
    print(f"Step setting: {step}")
    positions = []
    for i, position in enumerate(positions_list):
        # order positions by value
        if i == 0:
            position = sorted(position, key=itemgetter(5), reverse=True)[:step]
            positions.append(position)
        if i == 1:
            position = sorted(position, key=itemgetter(5), reverse=True)[:step]
            positions.append(position)
        if i == 2:
            position = sorted(position, key=itemgetter(5), reverse=True)[:step]
            positions.append(position)
        if i == 3:
            position = sorted(position, key=itemgetter(5), reverse=True)[:step]
            positions.append(position)
        if i == 4:
            position = sorted(position, key=itemgetter(5), reverse=True)[:step]
            positions.append(position)
    return positions


# def make_fanduel_team(league, player_picks):
#     teams = []
#     for possible_team in league:
#     #     possible_team = [i for i in possible_team]
#     #     for player in player_picks:
#     #         possible_team.extend([player])
#     #     positions = [i[1] for i in possible_team]
#         names = [i[2] for i in possible_team]
#     #     # general question: Which positions should have higher/lower asserted value ratings?
#         try:
#             assert len(names) == len(set(names))
#     #         assert positions.count('QB') == 1
#     #         assert positions.count('RB') >= 2 and positions.count('RB') <= 3
#     #         assert positions.count('WR') >= 3 and positions.count('WR') <= 4
#     #         assert positions.count('TE') >= 1 and positions.count('TE') <= 2
#     #         assert positions.count('D') == 1
#         except:
#             print(possible_team)
#             continue

#         salary = sum(map(lambda x: float(x[3]), possible_team))
#         fppg = sum(map(lambda x: float(x[4]), possible_team))
#         fppg = float("{:.2f}".format(fppg))
#         # if we don't include the fppg bit we miss tons of team configs... not sure why it matters
#         """
#         10/18
#         when > 130: 408,170
#         when > 2000: 408,170
#         when > 100: 408,170

#         when > 50: 182,502

#         when > 1: 6,635
#         when not set: 6,635

#         whhhhhyyyyyyy !!!????
#         """

#         if salary > 60000:
#             continue
#         elif salary <= 60000:
#             teams.append([fppg, salary, possible_team])
#     return teams
