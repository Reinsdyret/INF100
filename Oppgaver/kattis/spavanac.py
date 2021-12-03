"""https://open.kattis.com/problems/spavanac"""

def fourty_five_minutes_earlier(h,m):
    if m >= 45:
        newH = h
        newM = m - 45
    else:
        remaining_min = 45 - M
        if h == 0:
            newH = 23
        else:
            newH = h - 1
        newM = 60 - remaining_min

    return [str(newH),str(newM)]

H,M = map(int,input().split())

print(' '.join(fourty_five_minutes_earlier(H,M)))
