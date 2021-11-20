"""https://open.kattis.com/problems/sevenwonders"""


cardSet = {
    "T": 0,
    "G" : 0,
    "C" : 0
}

cards = input()

for card in cards:
    cardSet[card] += 1

sumPointsCard = cardSet["T"] ** 2 + cardSet["G"] ** 2 + cardSet["C"] ** 2

pointsPlayer = min([cardSet["T"],cardSet["G"],cardSet["C"]]) * 7

print(sumPointsCard + pointsPlayer)
