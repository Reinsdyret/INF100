"""Write a function write_to_csv(filename, list_of_rows) that writes the the rows given in the file given"""
import csv

def write_to_csv(filename,list_of_rows):
    with open(filename,"w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(list_of_rows)
