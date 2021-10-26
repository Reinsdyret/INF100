"""Do same as oppg_1 just put >>> in front of each line and <<< behind"""
# Used for getting path of file
import os.path

def open_file(filename:str) -> str:
    """Function that opens a txt file and returns a string identical to the contents"""
    file_string = ""
    with open(os.path.dirname(__file__) + "/" + filename,"rt", encoding="utf-8") as textfile:
        for line in textfile:
            line = line.strip("\n")
            file_string += f">>>{line}<<<\n"
    return file_string

print(open_file("askeladden.txt"))
