"""https://open.kattis.com/problems/provincesandgold"""

gold, silver, copper = map(int,input().split(" "))

costs = {
    "gold" : 6,
    "silver" : 3,
    "copper" : 0,
    "province" : 8,
    "duchy" : 5,
    "estate" : 2
}

worths = {
    "gold" : 3,
    "silver" : 2,
    "copper" : 1,
    "province" : 6,
    "duchy" : 3,
    "estate" : 1
}

sum_buying_power = (worths["gold"] * gold) + (worths["silver"] * silver) + (worths["copper"] * copper)

if sum_buying_power < costs["estate"]:
    output = "Copper"
elif sum_buying_power < costs["duchy"]:
    if sum_buying_power in [3,4]:
        output = "Estate or Silver"
    else:
        output = "Estate or Copper"
elif sum_buying_power < costs["province"]:
    if sum_buying_power == 5:
        output = "Duchy or Silver"
    else:
        output = "Duchy or Gold"
else:
    output = "Province or Gold"

print(output)
