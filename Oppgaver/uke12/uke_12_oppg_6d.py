
import csv

lats = []
lons = []

with open('Akvakulturregisteret.csv', newline='', encoding='iso-8859-1') as csvfile:
    akvareader = csv.reader(csvfile, delimiter=';')
    for row in akvareader:
        try:
            lat = float(row[-2]) # latitude is second last
            lon = float(row[-1]) # longitude is last
        except ValueError:
            continue
        lats.append(lat)
        lons.append(lon)

try:
    import matplotlib.pyplot as plt
    # Plot only points under 10 or over 20 lons with color, others invisible
    for i in range(len(lons)):
        if lons[i] < 10 or lons[i] > 20:
            plt.plot(lons[i],lats[i],'+r')
            continue
        plt.plot(lons[i],lats[i],'+w')
    plt.show()
    plt.savefig("uke_12_oppg_6d.png")
except (ImportError, ModuleNotFoundError) as e:
    print(f'Import of matplotlib failed: {e}')
    print(f'We have {len(lats)} latitudes and {len(lons)} longitudes')
