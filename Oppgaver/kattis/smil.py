"""https://open.kattis.com/problems/smil"""

input_smiles = input()
smiles = [":)",";)",":-)",";-)"]
smile_indexes = []

for i in range(len(input_smiles)):
    if input_smiles[i:i+2] in smiles or input_smiles[i:i+3] in smiles:
        smile_indexes.append(i)

for smile_index in smile_indexes: print(smile_index)
