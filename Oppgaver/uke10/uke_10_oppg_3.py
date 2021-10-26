"""Write function r_w_file(infile,outfile) that takes in file of temps
and writes to outfile every temp with temp higher than or equal to 23.5.
If there are no temps over 23.5 the outfile will be empty"""

# Used for getting path of file
#import os.path

def r_w_file(infile,outfile:str) -> None:
    """Takes in file "infile" containing days:temperatures and creates a new file "outfile"
    where all temperatures from infile that are higher than or equal to 23.5"""

    # String to be written to outfile
    outstring = ""
    # Os.path stuff just says the path of this file
    # with open(os.path.dirname(__file__) + "/" + infile,"r", encoding="utf-8") as data:
    with open(infile,"r",encoding="utf-8") as data:
        for line in data:
            day, temp = line.split(" ")
            if float(temp) >= 23.5:
                outstring += f"{day} {temp}"

    # with open(os.path.dirname(__file__) + "/" + outfile,"w", encoding="utf-8") as writing:
    with open(outfile,"w", encoding="utf-8") as writing:
        writing.write(outstring)
