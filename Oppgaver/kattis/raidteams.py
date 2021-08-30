"""
There is an upcoming raid event in an online game. You are the leader of a guild with N adventurers. In this game, 
every adventurer has a rating S for each of the 3 skills that every adventurer must learn. A high S value indicates mastery at that skill. 
You wish to group the adventurers into raid teams using the following steps:

Amongst all currently available adventurers, the adventurer with the highest S value for the first skill is selected. In cases of ties, 
the adventurer with the lexicographically smallest name is selected. That adventurer is no longer available from now on.

The same selection criteria is applied for the second and third skill in order.

These three adventurers will form a raid team.

The process repeats starting from the first skill until no more teams of three can be formed. 
There could be situations where some players are not part of any raid teams. They will stay behind and guard the guild hall during the event.

Report the members of every newly-created raid team, in the order which the teams were formed. All N adventurers are available initially.

Input
The first line of the input contains an integer N (3≤N≤100000). N lines follow, 
each line beginning with the name of the adventurer followed by three integers S1S2S3 (0≤S1,S2,S3≤2000000000) 
describing the level of proficiency of the adventurer in the three skills in order.
 All names are non-empty alphanumeric string of at most 10 characters, and all names are unique.

Output
Whenever a raid team is formed, on a new line, output the three names of the adventurers of the new team from the lexicographically 
smallest name to the lexicographically largest name, with a single space between consecutive names.
"""
import sys
def get_players(): return list(map(str, sys.stdin.readline().strip().split()))
N = int(input())
players = []
S1 = []
S2 = []
S3 = []
raidTeams = []
for i in range(0,N):
    player = get_players()
    players.append(player[0])
    S1.append(int(player[1]))
    S2.append(int(player[2]))
    S3.append(int(player[3]))

def make_raid_team():
    global players, S1, S2, S3
    a = [S1[0],0]
    for i in range(1,len(players)):
        if a[0] < S1[i]:
            a = [S1[i],i]
            continue
        if a[0] == S1[i]:
            if players[a[1]] > players[i]:
                a = [S1[i],i]
                continue
    aName = players[a[1]]
    players.pop(a[1])
    S1.pop(a[1])
    S2.pop(a[1])
    S3.pop(a[1])

    b = [S2[0],0]
    for i in range(1,len(players)):
        if b[0] < S2[i]:
            b = [S2[i],i]
            continue
        if b[0] == S2[i]:
            if players[b[1]] > players[i]:
                b = [S2[i],i]
                continue
    bName = players[b[1]]
    players.pop(b[1])
    S1.pop(b[1])
    S2.pop(b[1])
    S3.pop(b[1])
    c = [S3[0],0]
    for i in range(1,len(players)):
        if c[0] < S3[i]:
            c = [S3[i],i]
            continue
        if c[0] == S3[i]:
            if players[c[1]] > players[i]:
                c = [S3[i],i]
                continue
    cName = players[c[1]]
    players.pop(c[1])
    S1.pop(c[1])
    S2.pop(c[1])
    S3.pop(c[1])
    return [aName,bName,cName]

def fast_out(arr):
    sys.stdout.write(
        " ".join(map(str, arr)) + "\n"
    )



while len(players) > 2:
    team = make_raid_team()
    #team.sort()
    low = min(team)
    high = max(team)
    newTeam = [low, 0, high]
    team.pop(team.index(low))
    team.pop(team.index(high))
    newTeam[1] = team[0]
        
    raidTeams.append(newTeam)


for i in range(0,len(raidTeams)):
    fast_out([raidTeams[i][0],raidTeams[i][1],raidTeams[i][2]])
