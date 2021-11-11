# Lage filer til innlevering i INF100
# ℘

# --------------------------------------
import os

# inputs
uke_nr = input("Uke nummer: ")
oppg_nr = input("Oppgave antall: ")
dir_name = input("Mappe navn: ")
print(" --- Custom header: €header")
print(" --- Printes på toppen av siden som | #€header |")
print(
    " --- f.eks: hvis [€header = INF100] --> | #INF100 | (# auntomatisk inkludert, kan være tom)"
)
header = input("Egenfindert headder: ")

# --------------------------------------

# Lager mappe
os.mkdir(dir_name)
os.chdir(dir_name)
# fix number
if len(uke_nr) < 2:

    uke_nr = int(f"0{uke_nr}")

# turn intager
oppg_nr = int(oppg_nr)

# make files
for i in range(0, oppg_nr):

    name = f"uke_{uke_nr}_oppg_{i+1}.py"  # compile name

    with open(name, "a") as wr:

        if header != "":  # check if empty

            wr.write(f"#{header}")  # write to file


# -------------------------------------------------------------------------------------------------
# Endre hva enn du vil og redistruber som du vil, bare legg til et symbol på linje 2. Because why not.

# --- notes
# Filer havner et lag ut i mappene, pga. python nonsense. Finnes nokk en måte å fikse det.
# Lager ikke en mappe til å putte dem i, så du bare flytter filene du får til der du vil ha dem.
