"""https://open.kattis.com/problems/parking2"""

def handle_case(parkings:list) -> int:
    distanse = 0
    sorted_parkings = sorted(parkings)
    parking_slot = int(round(sorted_parkings[-1] + sorted_parkings[0]) /2)
    distanse += parking_slot -  sorted_parkings[0] + sorted_parkings[-1] - parking_slot
    for i in range(1,len(sorted_parkings)):
        distanse += sorted_parkings[i] - sorted_parkings[i-1]
    return distanse

cases = int(input())
answers = []

for case in range(cases):
    stores = int(input())
    locations = map(int,input().split(" "))
    answers.append(handle_case(locations))

for answer in answers: print(answer)