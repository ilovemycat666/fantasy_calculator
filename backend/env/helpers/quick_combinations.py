from itertools import combinations

def quick_combinations(shorter_roster_by_position, player_picks):
    # if len(player_picks) == 0:
    #     QB = shorter_roster_by_position[0]
    #     RB = shorter_roster_by_position[1]
    #     WR = shorter_roster_by_position[2]
    #     TE = shorter_roster_by_position[3]
    #     D = shorter_roster_by_position[4]

    #     RB_set_two = list(combinations(RB, 2))
    #     WR_set_three = list(combinations(WR, 3))
    #     FLEX = []
    #     FLEX.extend(WR)
    #     FLEX.extend(RB)
    #     FLEX.extend(TE)
        

    #     teams = []
    #     for q in QB:
    #         for r in RB_set_two:
    #             for w in WR_set_three:
    #                 for t in TE:
    #                     for f in FLEX:
    #                         if f in r or f in w or f in t:
    #                             continue
    #                         for d in D:
    #                             teams.append([q, r[0], r[1], w[0], w[1], w[2], t, f, d]) 



    #     return teams  

    # else:


    QB = []
    RB = []
    WR = []
    TE = []
    FLEX = []
    D = []

    pick_QB = []
    pick_RB = []
    pick_WR = []
    pick_TE = []
    pick_D = []

    for player in player_picks:
        position = player[1]
        if position == "QB":
            pick_QB.append(player)
        elif position == "D":
            pick_D.append(player)
        elif position == "RB":
            pick_RB.append(player)
        elif position == "WR":
            pick_WR.append(player)
        elif position == "TE":
            pick_TE.append(player)

# ----- Quarterback ----- # 
    if len(pick_QB) == 0:
        QB = shorter_roster_by_position[0]
    if len(pick_QB) == 1:
        QB = pick_QB

# ----- Runningback ----- # 

    if len(pick_RB) == 0:
        RB = list(combinations(shorter_roster_by_position[1], 2))
    elif len(pick_RB) == 1:
        for i in shorter_roster_by_position[1]:
            RB.append([i, pick_RB[0]])
    elif len(pick_RB) == 2:
        RB = pick_RB
    elif len(pick_RB) == 3:
        RB.append(pick_RB[0])
        RB.append(pick_RB[1])
        FLEX.append(pick_RB[2])

# ----- Wide Receiver ----- # 

    if len(pick_WR) == 0:
        WR = list(combinations(shorter_roster_by_position[2], 3))
    elif len(pick_WR) == 1:
        WR = list(combinations(shorter_roster_by_position[2], 2))
        WR = [list(i) for i in WR]
        for i in WR:
            i.extend(pick_WR)
    elif len(pick_WR) == 2:
        for i in shorter_roster_by_position[2]:
            WR.append([i, pick_WR[0], pick_WR[1]])
    elif len(pick_WR) == 3:
        WR = pick_WR
    elif len(pick_WR) == 4:
        WR.append(pick_WR[0])
        WR.append(pick_WR[1])
        WR.append(pick_WR[2])
        FLEX.append(pick_WR[3])

# ----- Tight End ----- # 

    if len(pick_TE) == 0:
        TE = shorter_roster_by_position[3] 
    elif len(pick_TE) == 1:
        TE = pick_TE
    elif len(pick_TE) == 2:
        TE = pick_TE[0]
        FLEX = pick_TE[1]

# ----- FLEX ----- # 
    
    if len(FLEX) == 0:
        if len(RB) != 2:
            FLEX.extend(shorter_roster_by_position[1])
        if len(WR) != 3:
            FLEX.extend(shorter_roster_by_position[2])
        if len(TE) != 1:
            FLEX.extend(shorter_roster_by_position[3])

# ----- Defence ----- # 

    if len(pick_D) == 0:
        D = shorter_roster_by_position[4]
    if len(pick_D) == 1:
        D = pick_D

# ----- Team Building ----- # 

    teams = []
    for q in QB:
        for r in RB:
            for w in WR:
                for t in TE:
                    for f in FLEX:
                        if f in r or f in w or f == t:
                            continue
                        for d in D:
                            team = [q, r[0], r[1], w[0], w[1], w[2], t, f, d]
                            salary = sum(map(lambda x: float(x[3]), team))
                            fppg = sum(map(lambda x: float(x[4]), team))
                            fppg = float("{:.2f}".format(fppg))
                            
                            if salary <= 60000:
                                teams.append([fppg, salary, team])
    return teams