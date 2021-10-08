"""
Make a function render_plot() that takes in a list of coordinates in tuple form and renders a plot of these coordinates as *.
The plot should be as small as possible, causing the plot to have no empty rows or columns.
The plot should also have hashtags # around it.
The function will return the plot as a string
"""

def render_plot(coordinates:list) -> str:
    """Function taking in a list of coordinates as tuples and returns a plot with the coordinates as *. With frame as #"""
    plot = ""
    #Find min and max coordinates
    minX, minY = coordinates[0]
    maxX, maxY = coordinates[0]
    for x, y in coordinates:
        minX = x if minX > x else minX
        maxX = x if maxX < x else maxX
        minY = y if minY > y else minY
        maxY = y if maxY < y else maxY
    #Defining width of the frame
    width = maxX - minX

    #Making first and last row of #
    topAndBottomFrame = "#" * (width + 3)

    #Making string of points and spaces
    points = ""
    for y in range(maxY,minY-1,-1):
        points += "#"
        for x in range(minX,maxX+1):
            points += "*" if (x,y) in coordinates else " "
        points += "#"
        points += "\n"

    #Putting it all together
    plot += topAndBottomFrame + "\n"
    plot += points
    plot += topAndBottomFrame
    
    return plot
