"""https://open.kattis.com/problems/speeding"""
import math

def calculate_average_mph(deltaTime:int, deltaDistance:int) -> float:
    return math.floor(deltaDistance / deltaTime)

n = int(input())
last_time_and_distance = []

for i in range(n):
    last_time_and_distance.append(list(map(int,input().split(" "))))


average_speeds = [calculate_average_mph(last_time_and_distance[i][0] - last_time_and_distance[i-1][0],last_time_and_distance[i][1] - last_time_and_distance[i-1][1]) for i in range(1,len(last_time_and_distance))]
max_average_speed = max(average_speeds)

print(max_average_speed)
