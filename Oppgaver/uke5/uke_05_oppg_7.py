"""
I filen uke_05_oppg_7.py skriv en funksjon som heter hyd_pres() og som beregner trykket på en gitt dybde i enheten dbar. 
Argumentene til funksjonen skal være: en densitetsverdi (p), tyngdekraftens akselerasjon (g) og dybden (z).
"""

def hyd_pres(p,g,z):
    """Function taking in parameters density(p), gravity acceleration(g) and depth(z) and returns the pressure of the depth as decibar (10^(-4))"""
    return (p*g*z) * 10**-4 
