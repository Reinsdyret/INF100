"""
Make a function that takes in a list of integers and returns a string of a starmade bar chart, where each bar represents an integer in the array
"""


#Taking use of function from question 2
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


def render_histogram(histogram:list) -> str:
    """Takes in list of integers and returns string of a starmade bar chart, where each bar represents an integer in the array"""
    maxHeight = max(histogram)

    # Creating 2d matrix with none as values found on: https://stackoverflow.com/questions/4230000/creating-a-2d-matrix-in-python  
    histogramBars = [[None for _ in range(maxHeight)] for _ in range(len(histogram))]

    for i in range(len(histogram)):
        for p in range(maxHeight - histogram[i]):
            histogramBars[i][p] = " "
        for p in range(maxHeight-histogram[i], maxHeight):
            histogramBars[i][p] = "*"

    return render_image(histogramBars)
