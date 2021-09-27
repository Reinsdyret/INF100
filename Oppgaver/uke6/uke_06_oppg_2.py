"""
Predefined array is of string 0s and 1s making a heart, but rotated 90 degrees against the clock. The wanted output is a heart of 0s
In the question text x and y is used opposite of what they actually are,
I will use the same just because
"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#for x in range(len(grid)):
#    for y in range(len(grid[x])):

for i in range(len(grid)):
    