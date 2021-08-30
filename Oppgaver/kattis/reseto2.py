'''
line = input()
words = line.split()
N = int(words[0])
K = int(words[1])
'''
N, K = map(int, input().split())

composite = [0] * (1+N)

crossed_count = 0

def cross(x):
    global crossed_count
    if composite[x]: return


    composite[x] = 1
    crossed_count += 1
    if crossed_count == K:
        print(x)
        exit(0)



for p in range(2, N+1):
    if composite[p]:
        continue

    cross(p)

    for x in range(p*p, N+1, p):
        cross(x)