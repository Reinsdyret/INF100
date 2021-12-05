"""Uses the file "NO_ADM12.csv to give information on municipalities within counties in Norway"""
import csv

def get_data(filename:str) -> list:
    """Get counties and municipalities from filename with structure like file \"NO_ADM12.csv\""""
    # Init dictionaries
    # counties = "code": "county"
    counties = dict()
    # municipalities = "municipality" : "population"
    municipalities = dict()

    # Open file and sort data
    with open(filename, 'r') as f:
        file_reader = csv.reader(f,delimiter=';')
        for row in file_reader:
            if row[1] == 'name': continue
            county_or_municipality = row[1]
            feature_code = row[5]
            adm1_code = row[7]
            population = row[9]
            if feature_code == "ADM1":
                counties[adm1_code] = county_or_municipality
            elif feature_code == "ADM2":
                municipalities[county_or_municipality] = [int(population),adm1_code]
    return [counties,municipalities]
    
def five_small_and_largest_municipalities(municipalities:dict) -> list:
    """Returns the five smallest and largest municipalities"""
    # Get a sorted list of municipalities
    sorted_municipalities = sorted(municipalities, key=municipalities.get)
    return sorted_municipalities[:5] + sorted_municipalities[-5:]


def print_fylke(num:str) -> None:
    """Prints all municipalities with habitants in a given county code"""
    data = get_data("NO_ADM12.csv")
    county = data[0][num]
    municipalities = data[1]
    municipalities_in_county = {}
    for k, v in municipalities.items():
        if v[1] == num:
            municipalities_in_county[k] = v[0]

    sorted_municipalities = sorted(municipalities_in_county)
    print("==========================")
    print(f"{num} {county}")
    print("==========================")
    for muni in sorted_municipalities:
        print(f"{muni:<15}{municipalities_in_county[muni]:>11}")

def find_fylke(term:str):
    """Takes in a term and searching for fylke containing this, returns fylke code"""
    counties = get_data("NO_ADM12.csv")[0]
    for k,v in counties.items():
        if term in v:
            return k
    
    return False


data = get_data("NO_ADM12.csv")

all_municipalities = data[1]

# Print largest and smallest municipalities
small_and_large_municipalities = five_small_and_largest_municipalities(all_municipalities)
print("De fem største kommunene er:")
print(" ".join(small_and_large_municipalities[5:]))
print("De fem minste kommunene:")
print(" ".join(small_and_large_municipalities[:5]))

while True:
    term = input("Search word [q to quit]? ")
    code = find_fylke(term)

    if term == 'q':
        break

    if not code:
        print("No matching fylke found. Try again")
        continue

    print_fylke(code)
