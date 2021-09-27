"""
I filen uke_05_oppg_6.py skriv en funksjon som heter hvem_eldst() som tar som input fire argumenter:
navnet på første personen (string), alderen på første personen (int), navnet på andre personen (string), 
alderen på andre personen (int). Funksjonen bestemmer siden hvem som er eldre og 
returnerer en setning som angir navn og alder på den eldste personen enligt følgende eksempel: 
hvem_eldst("Ola", 43, "Katrine", 23) skal returnere strengen "Ola er 43 år og eldst."
"""

def hvem_eldst(name1,age1,name2,age2):
    """Function takes in name and age for two different people and returns string with the oldest person"""
    lookup = {
        age1: name1,
        age2: name2}
    max_age = max(age1,age2)
    return f"{lookup[max_age]} er {max_age} år og eldst."
