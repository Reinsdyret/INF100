"""Write a function that takes in filename.txt as parameter and
returns a string identical to the file"""
# Used for getting path of file
#import os.path

def open_file(filename:str) -> str:
    """Function that opens a txt file and returns a string identical to the contents"""
    file_string = ""
    # Os.path stuff just says the path of this file
    # with open(os.path.dirname(__file__) + "/" + filename,"rt", encoding="utf-8") as textfile:
    with open(filename,"r",encoding="utf-8") as textfile:
        for line in textfile:
            file_string += line
    return file_string
