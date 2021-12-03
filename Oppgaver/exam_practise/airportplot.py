import csv
import matplotlib.pyplot as plt

def gather_data(filename):
    """Function for gathering the data from a csv file and cols 1,9,11"""
    types = []
    iatas = []
    coords = []
    with open(filename, "r") as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        for row in datareader:
            if row[1] == "type":
                continue
            types.append(row[1])
            iatas.append(row[9])
            coords.append(row[11])
    return [types,iatas,coords]

def handle_coords(coords):
    xs = []
    ys = []
    for coord in coords:
        x, y = coord.split(",")
        y = y.strip()
        xs.append(float(x))
        ys.append(float(y))

    return [ys,xs]


def handle_types(types):
    """Function for handling the types and returning in excact point size"""
    sizes = []
    for airport_type in types:
        if airport_type == "medium_airport":
            sizes.append(2)
            continue
        sizes.append(4)

    return sizes


def plot_points_iatas(sizes,iatas,types,coords):
    """Function for plotting the airport data, coords should be prehandled""" 
    # Plot points
    xs = coords[0]
    ys = coords[1]
    plt.scatter(xs,ys,s=sizes,c="orange")
    for i in range(len(iatas)):
        x = coords[0][i]
        y = coords[1][i]
        iata = iatas[i]
        airport_type = types[i]
        if airport_type == "large_airport":
            plt.annotate(iata,(x,y))

def set_title_and_axis(title,xaxis,yaxis):
    """Set title for plot and xaxis and yxaxis info"""
    plt.title(title)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)

data = gather_data("airport-codes.csv")

handled_coords = handle_coords(data[2])

sizes = handle_types(data[0])

plot_points_iatas(sizes,data[1],data[0],handled_coords)

title = "Airports"
xlabel = "Longitude"
ylabel = "Latitude"
set_title_and_axis(title,xlabel,ylabel)

plt.show()
