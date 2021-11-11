"""Write function read_first_col() that writes out the first column of a the file 2019-06-01_Oslo.csv"""
import csv

def read_first_col():
    with open("2019-06-01_Oslo.csv","r") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter = " ")
        for row in csv_reader:
            print(row[0])

read_first_col()
