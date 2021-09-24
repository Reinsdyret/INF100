"""
I denne oppgaven skal vi fortsette med konverteringen fra stones og pounds til kilograms som vi gjorde uke 2 i oppgave 3, 
men denne gangen skal vi bruke funksjoner.
"""

def stones_to_pounds(stone):
    return stone * 14


def stones_to_kg(stone):
    return stone/0.15747


def pounds_to_kg(pounds):
    return pounds/2.20462


def imperial_to_metric(stone,pound):
    return round((stones_to_kg(stone) + pounds_to_kg(pound)),2)

print(imperial_to_metric(12, 4))