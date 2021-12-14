def make_stats(matches):
    teams = {} # dict of dicts: name -> {GF, GA, GD, PT}
    ########## vvvvvv edit this part vvvvvvv ##############
    # real team names should be taken from the "matches" list
    # and the following filled in
    # GF: goals for the team
    # GA: goals agains the team
    # GD: goal difference, always the same as GF-GA
    # PT: points: 3 for win, 1 for draw
    # A list of all teamnames
    teams_list = []
    
    for team, team2, _, _ in matches:
        teams_list.append(team)
        teams_list.append(team2)
    
    # Make teams_list into a set and back into list to remove any duplicates
    teams_list = list(set(teams_list))

    teams[teams_list[0]] = {'GF':0, 'GA':0, 'GD':0, 'PT':0}
    teams[teams_list[1]] = {'GF':0, 'GA':0, 'GD':0, 'PT':0}
    teams[teams_list[2]] = {'GF':0, 'GA':0, 'GD':0, 'PT':0}
    teams[teams_list[3]] = {'GF':0, 'GA':0, 'GD':0, 'PT':0}

    # Loop over matches and change statistics based on results
    for team1, team2, goals_team1, goals_team2 in matches:
        # Add the goals scored by the teams
        teams[team1]['GF'] += goals_team1
        teams[team2]['GF'] += goals_team2
        # Add the goals scored against the teams
        teams[team1]['GA'] += goals_team2
        teams[team2]['GA'] += goals_team1
        
        # Calculate points won and add to dict
        if goals_team1 == goals_team2:
            # Draw
            teams[team1]['PT'] += 1
            teams[team2]['PT'] += 1
        elif goals_team1 > goals_team2:
            # Team1 won
            teams[team1]['PT'] += 3
        else:
            # Team2 won
            teams[team2]['PT'] += 3
    
    # Loop over teams and calculate and change GD
    for team in teams.keys():
        teams[team]['GD'] = teams[team]['GF'] - teams[team]['GA']


    ########## ^^^^^^ edit this part ^^^^^^^ ##############
    return teams


# an example for the "matches" datastructure
FIFA_1998_A = [
    ("Brazil", "Scotland", 2, 1),
    ("Morocco", "Norway", 2, 2),
    ("Scotland", "Norway", 1, 1),
    ("Brazil", "Morocco", 3, 0),
    ("Brazil", "Norway", 1, 2),
    ("Scotland", "Morocco", 0, 3),
]

# make_stats(FIFA_1998_A) takes this ^^^^ 
# and the return value should be 

FIFA_1998_A_data = { 
    'Brazil': {'GF': 6, 'GA': 3, 'GD': 3, 'PT': 6}, 
    'Scotland': {'GF': 2, 'GA': 6, 'GD': -4, 'PT': 1},
    'Morocco': {'GF': 5, 'GA': 5, 'GD': 0, 'PT': 4},
    'Norway': {'GF': 5, 'GA': 4, 'GD': 1, 'PT': 5}
}

# checking the return value matches what we expect
if make_stats(FIFA_1998_A) == FIFA_1998_A_data:
    print("make_stats looks good, you can remove the exit() line now!\n\n\n")
else:
    print("Something is wrong in make_stats")




def compare(matches, data, a, b):
    """
    Compare two team _names_ a and b. 
    matches is a list of match results.
    data is the result of make_stats(matches).
    
    If a is ranked higher, return 1
    If b is ranked higher, return -1
    If a and b are undecided, print f"LOTTERY {a} {b}" and return 0
    
    Sequence for ranking (go to the next rule if the two teams are equal)
    (1) The higher points score PT wins
    (2) The higher goal difference GD wins
    (3) The higher "goals for" GF wins
    (4) The winner of the direct match between the two teams
        (we will ignore the situation where 3 teams are equal)
    (5) Lottery draw
    """
    ########## vvvvvv edit this part vvvvvvv ##############
    # right now, the team names get ranked based on alphabet
    # need to fix this
    if data[a]['PT'] > data[b]['PT']:
        # Team a has higher points than team b
        return 1
    elif data[b]['PT'] > data[a]['PT']:
        # Team b has higher points than team a
        return -1
    
    # Points are even
    # Test for winner of largest goal difference
    if data[a]['GD'] > data[b]['GD']:
        # Team a has higher goal difference than team b
        return 1
    elif data[b]['GD'] > data[a]['GD']:
        # Team b has higher goal difference than team a
        return -1
    
    # Goal difference is even
    # Test for winner of most scored goals
    if data[a]['GF'] > data[b]['GF']:
        # Team a has scored more goals than team b
        return 1
    elif data[b]['GF'] > data[a]['GF']:
        # Team b has scored more goals than team a
        return -1
    
    # Goals scored is even
    # Test for winner of the the match between the two
    # Find match where they played
    for team1, team2, goals_team1, goals_team2 in matches:
        # Check for team1 = a and team2 = b
        if team1 == a and team2 == b:
            # We have found the match where team1 is a and team2 is b
            if goals_team1 > goals_team2:
                # Team a won against team b in the match
                return 1
            elif goals_team2 > goals_team1:
                # Team b won against team a in the match
                return -1
        # Check for team1 = b and team2 = a
        elif team1 == b and team2 == a:
            # We have found the match where team1 is b and team2 is a
            if goals_team2 > goals_team1:
                # Team a won against team b in the match
                return 1
            elif goals_team1 > goals_team2:
                # Team b won against team a in the match
                return -1

    # The match between the two was a draw
    print(f"LOTTERY {a} {b}")
    return 0
    ########## ^^^^^^ edit this part ^^^^^^^ ##############
    

######################################################
############# nothing to edit below here #############
############ some more examples for testing ##########
######################################################

FIFA_1994_D = [
    ("Argentina", "Greece", 4, 0),
    ("Nigeria", "Bulgaria", 3, 0),
    ("Argentina", "Nigeria", 2, 1),
    ("Bulgaria", "Greece", 4, 0),
    ("Argentina", "Bulgaria", 0, 2),
    ("Greece", "Nigeria", 0, 2),
]

FIFA_1994_D_data = {
    'Argentina': {'GF': 6, 'GA': 3, 'GD': 3, 'PT': 6}, 
    'Greece': {'GF': 0, 'GA': 10, 'GD': -10, 'PT': 0}, 
    'Nigeria': {'GF': 6, 'GA': 2, 'GD': 4, 'PT': 6}, 
    'Bulgaria': {'GF': 6, 'GA': 3, 'GD': 3, 'PT': 6},
}

FIFA_1994_E = [
    ("Italy", "Ireland", 0, 1),
    ("Norway", "Mexico", 1, 0),
    ("Italy", "Norway", 1, 0),
    ("Mexico", "Ireland", 2, 1),
    ("Italy", "Mexico", 1, 1),
    ("Ireland", "Norway", 0, 0),
]

FIFA_1994_E_data = {
    'Italy': {'GF': 2, 'GA': 2, 'GD': 0, 'PT': 4}, 
    'Ireland': {'GF': 2, 'GA': 2, 'GD': 0, 'PT': 4}, 
    'Norway': {'GF': 1, 'GA': 1, 'GD': 0, 'PT': 4}, 
    'Mexico': {'GF': 3, 'GA': 3, 'GD': 0, 'PT': 4},
}


FIFA_1990_F = [
    ("England", "Ireland", 1, 1),
    ("Netherlands", "Egypt", 1, 1),
    ("England", "Netherlands", 0, 0),
    ("Ireland", "Egypt", 0, 0),
    ("England", "Egypt", 1, 0),
    ("Ireland", "Netherlands", 1, 1),
]

FIFA_1990_F_data = {
    'England': {'GF': 2, 'GA': 1, 'GD': 1, 'PT': 5}, 
    'Ireland': {'GF': 2, 'GA': 2, 'GD': 0, 'PT': 3}, 
    'Netherlands': {'GF': 2, 'GA': 2, 'GD': 0, 'PT': 3}, 
    'Egypt': {'GF': 1, 'GA': 2, 'GD': -1, 'PT': 2},
}

from functools import cmp_to_key, partial

def pretty(order, data):
    print(f"{' ':14} {'GF':>3} {'GA':>3} {'GD':>3}   {'PT':>3}")
    for team in order:
        k = team
        v = data[team]    
        print(f"{k:14} {v['GF']:3d} {v['GA']:3d} {v['GD']:3d}   {v['PT']:3d}")
    print("-"*20)

all_groups = [FIFA_1998_A, FIFA_1994_D, FIFA_1994_E, FIFA_1990_F]
all_data = [FIFA_1998_A_data, FIFA_1994_D_data, FIFA_1994_E_data, FIFA_1990_F_data]

expected = [
    ['Brazil', 'Norway', 'Morocco', 'Scotland'],
    ['Nigeria', 'Bulgaria', 'Argentina', 'Greece'],
    ['Mexico', 'Ireland', 'Italy', 'Norway'],
    ['England', 'Ireland', 'Netherlands', 'Egypt'],
]

for matches,data,ex in zip(all_groups,all_data,expected):
    order = sorted(data, key=cmp_to_key(partial(compare,matches,data)), reverse=True)
    pretty(order, data)
    if order == ex:
        print("This looks good!\n\n\n")
    else:
        print(f"!!! expected {ex}, but got {order}")
        
    
