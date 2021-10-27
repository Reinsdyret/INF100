"""Input is :
first line C(0<C<=100) that is the cost to sow one square metre
Second line L is the number of lawns to sow
The following L lines contain the length and width of lawns
Output how much it costs to sow all lawns"""

C = float(input())
L = int(input())
total_areal = 0

for i in range(L):
    length, width = map(float,input().split(" "))
    total_areal += length * width

print(total_areal * C)
