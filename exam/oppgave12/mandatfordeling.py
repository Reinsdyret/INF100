"""Exam 6th December 2021"""
import collections
import csv

def get_dictrict_fordelingstall(filename:str) -> dict:
    """Gathers the district, area and population count and calculate fordelingstall from a file with similar structure to \"valgdistrikt_2020-01-01.csv\"
    Returns dictionary with structure (district: fordelingstall)"""
    # Data dictionary where all data from file will be stored
    data = dict()
    # Opening of file
    with open(filename, 'r', encoding='UTF-8') as f:
        # Csv reader is needed as file is of type csv
        data_reader = csv.reader(f, delimiter=',')
        # Skip first row in csv file as this is headers
        next(data_reader)

        # Loop through all rows of the file
        for row in data_reader:
            # Calculate fordelingstall
            fordelingstall = int(row[1]) + (int(row[2]) * 1.8)
            # Put data into dictionary with fordelingstall
            data[row[0]] = fordelingstall

    return data

def mandatfordeling(filnavn:str, antall_mandater:int) -> collections.Counter:
    """Calculates the distribution of mandates based on data from file and amount of mandates to distribute
    Returns a Counter with structure such that Counter[district] = mandates_of_district"""
    # Get dictionary of districts and their corresponding fordelingstall
    districts = get_dictrict_fordelingstall(filnavn)
    # Set maximum amount of divisors for the calculation
    DIVISORS = antall_mandater
    # Create dictionary that will contain quotients from the calculation, structure like quotients[district] = list_of_quotients
    quotients = dict()

    # Calculate and add quotients to dictionary
    for key, fordelingstall in districts.items():
        list_of_quotients = []
        # Loop through all divisors and do calculation
        for divisor in range(DIVISORS):
            divisor = 2 * divisor + 1
            list_of_quotients.append(fordelingstall / divisor)
        # Add results to the dictionary
        quotients[key] = list_of_quotients
    
    # List with structure [(district,qoutient)] for all quotients
    district_quotient_list = []
    # Loop through and add all single quotient with their district
    for key, quotient_list in quotients.items():
        # Loop through the quotient list of the district
        for i in range(len(quotient_list)):
            # Add to the district_quotient list
            district_quotient_list.append(tuple((key,quotient_list[i])))

    # Sort the district_quotient list based on the quotient size, use of sorted found on stack overflow answered by cheeken: https://stackoverflow.com/a/10695161 
    sorted_district_quotient_list = sorted(district_quotient_list, key=lambda x: x[1],reverse=True)

    # List to append districts who get a mandate to
    mandates = []

    # Loop through the first antall_mandater elements and add districts to mandates list
    for i in range(antall_mandater):
        district, _ = sorted_district_quotient_list[i]
        mandates.append(district)

    # Return counter
    return collections.Counter(mandates)

#Get counter of mandates
mandate_count = mandatfordeling("valgdistrikt_2020-01-01.csv",169)

# Print put the information
header1 = "Distrikt"
header2 = "Mandater"
print(f"{header1:<11}{header2:>11}")
print("=" * 22)
for district, mandates in mandate_count.most_common():
    print(f"{district:<18}{mandates:>4}")
