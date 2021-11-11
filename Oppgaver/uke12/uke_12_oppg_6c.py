import csv

lats = []
lons = []
watertypes = []

with open("Akvakulturregisteret.csv", newline="", encoding="iso-8859-1") as csvfile:
    akvareader = csv.reader(csvfile, delimiter=";")
    for row in akvareader:
        try:
            lat = float(row[-2])  # latitude is second last
            lon = float(row[-1])  # longitude is last
            watertype = row[20]   # watertype is 20th
        except ValueError:
            continue
        lats.append(lat)
        lons.append(lon)
        watertypes.append(watertype)

try:
    import matplotlib.pyplot as plt
    for i in range(len(lons)):
        if watertypes[i] == "SALTVANN":
            plt.plot(lons[i], lats[i], "+r")
        else:
            plt.plot(lons[i], lats[i], "+b")
    
    plt.show()
    plt.savefig("uke_12_oppg_6c.png")
except (ImportError, ModuleNotFoundError) as e:
    print(f"Import of matplotlib failed: {e}")
    print(f"We have {len(lats)} latitudes and {len(lons)} longitudes")
