"""https://open.kattis.com/problems/pokerhand"""

five_hands = input().split(" ")
rank_list = []

for rank, suite in five_hands:
    rank_list.append(rank)

highest_rank_repitition = 0

for i in range(len(rank_list)):
    repitions = 0
    for p in range(i+1,len(rank_list)):
        if rank_list[i] == rank_list[p]:
            repitions += 1
    highest_rank_repitition = repitions if repitions > highest_rank_repitition else highest_rank_repitition

print(highest_rank_repitition + 1)