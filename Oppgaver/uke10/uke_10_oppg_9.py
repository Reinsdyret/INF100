"""Write function rename_from_data(filename) that takes in file
and makes a new file with the date and place gathered from the first two line
at the format YYYY-MM-DD_PLACENAME.txt"""
#import os.path

def rename_from_data(filename:str) -> None:
    """Makes a new file with the date and place gathered from the first two line
    at the format YYYY-MM-DD_PLACENAME.txt"""
    new_filename = ""
    #with open(os.path.dirname(__file__) + "/" + filename, "r", encoding="utf-8") as data:
    with open(filename,"r",encoding="utf-8") as data:
        first_two_lines = [next(data) for x in range(2)]
        place = first_two_lines[0].strip("\n")
        date = first_two_lines[1].strip("\n")
        new_filename = f"{date}_{place}.txt"
        # Os.path stuff just says the path of this file
        # with open(os.path.dirname(__file__) +"/" + new_filename,"w",encoding="utf-8") as new_file:
        with open(new_filename, "w", encoding="utf-8") as new_file:
            for line in data:
                new_file.write(line)

def rename_all(files:list) -> None:
    """Take in a list of files and run the rename_from_data function on all the files"""
    for each_file in files:
        rename_from_data(each_file)
