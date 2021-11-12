import csv

with open("Akvakulturregisteret.csv", newline="", encoding="iso-8859-1") as csvfile:
    akvareader = csv.reader(csvfile, delimiter=";")
    fishSpecies = {}
    for i in range(2):
        next(akvareader) # Skip the two first rows
    for row in akvareader:
        if row[12] in fishSpecies:
            fishSpecies[row[12]] += 1
            continue
        fishSpecies[row[12]] = 1
    
    # Sort the dictionary
    fishSpecies_list = sorted(fishSpecies.items(),key=lambda x: x[0])
    
    for fish, count in fishSpecies_list:
        print(f"{fish}: {count}")
