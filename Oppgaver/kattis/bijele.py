"""
One king
One queen
Two rooks
Two bishops
Two knights
Eight pawns

Mirko would like to know how many pieces of each type he should add or remove to make a valid set.

Input
The input consists of 6 integers on a single line, each between 0 and 10 (inclusive). 
The numbers are, in order, the numbers of kings, queens, rooks, bishops, knights and pawns in the set Mirko found.

Output
Output should consist of 6 integers on a single line; the number of pieces of each type Mirko should add or remove. If a number is positive, Mirko needs to add that many pieces. 
If a number is negative, Mirko needs to remove pieces."""

start = input().split()
for i in range(0,len(start)):
    start[i] = int(start[i])
goal = [1,1,2,2,2,8]
endString = ""

for i in range(0,len(goal)):
    goal[i] = goal[i] - start[i]
    endString += str(goal[i]) + " "

print(endString)
