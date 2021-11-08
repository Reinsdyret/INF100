"""https://open.kattis.com/problems/symmetricorder"""

def symmetric_list(arr:list) -> list:
    print(arr)
    arr.sort(key=len)
    pairs = []
    new_list = []
    print(arr)
    if len(arr) % 2 == 0:
        for i in range(0,len(arr),2):
            pairs.append([arr[i], arr[i+1]])
        for p1, p2 in pairs:
            new_list.append(p1)
        print(pairs)
        for i in range(len(pairs)-1,-1,-1):
            new_list.append(pairs[i][1])
    return new_list


a = int(input())
sets = []
while a != 0:
    set_a = []
    for i in range(a):
        set_a.append(input())
    sets.append(set_a)
    a = int(input())

new_sets = []

for set_b in sets:
    print(set_b)
    new_sets.append(set_b)

print(new_sets)

for i in range(len(new_sets)):
    print(f"SET {i+1}")
    for p in range(len(new_sets[i])):
        print(new_sets[i][p])
