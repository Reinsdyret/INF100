"""
I denne oppgaven skal vi dra tilbake til uke_02 og lage en ramme rundt ut en haiku. 
Derimot, denne gangen vil vi skrive dette som en funksjon, og vi skal ikke bruke print() i funksjonen.
"""

def draw_haiku_frame(line1,line2,line3):
    output_haiku = ""
    max_line = max([len(line1),len(line2),len(line3)]) + 4
    output_haiku += "@" * max_line + "\n"
    lines = [line1,line2,line3]
    for line in lines:
        output_haiku += "@ "
        spaces = max_line - len(line) - 4
        output_haiku += spaces * " "
        output_haiku += line
        output_haiku += " @\n"
    output_haiku += "@" * max_line
    return output_haiku

print(draw_haiku_frame("helo","I Am Lash", "Goodbye now"))