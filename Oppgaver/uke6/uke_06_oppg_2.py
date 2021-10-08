"""
Predefined array is of string 0s and 1s making a heart, but rotated 90 degrees against the clock. The wanted output is a heart of 0s
In the question text x and y is used opposite of what they actually are,
I will use the same just because
"""

def render_image(grid:list) -> str:
        """Function taking in a 2d array and returning a string of this array rotated -pi radians."""
        finishedString = ""
        columns = len(grid[0])
        for i in range(0,columns):
                finishedString += "\n" if i != 0 else ""
                column = [x[i] for x in grid]
                for i in column:
                        finishedString += i
        return finishedString
