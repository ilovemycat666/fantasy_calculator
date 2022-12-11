def picks(full_roster, picks):
    # while True:
    players = []
    bad_pick = []
    picks = picks.split(',')
    picks = [i.strip() for i in picks]

    if len(picks) > 9:
        bad_pick.append("You can only select 9 players")
        return players, bad_pick

    print("picks: ", picks)

    for pick in picks:
        player = [i for i in full_roster if i[2].lower() == pick.lower()]
        if not player and picks != ['']:
            bad_pick.append(pick)
        elif player:
            players.extend(player)
    
    if len(players) == len(picks) or picks == ['']:
        positions = [i[1] for i in players]
        print(positions)
        try:
            assert positions.count('QB') <= 1
            assert positions.count('RB') <= 3
            assert positions.count('WR') <= 4
            assert positions.count('TE') <= 2
            assert positions.count('D') <= 1
        except:
            bad_pick.append("Too many of one position")
        return players, bad_pick

    else:
        print("Misspelled or Unavailable Player Name. Try Again.")
        print("bad pick", bad_pick)
        return players, bad_pick