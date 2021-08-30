"""
Write down all integers between 2 and N, inclusive.

Find the smallest number not already crossed out and call it P; P is prime.

Cross out P and all its multiples that aren’t already crossed out.

If not all numbers have been crossed out, go to step 2.

Write a program that, given N and K, find the K-th integer to be crossed out.
Input
The integers N and K (1≤K<N≤100000).

Output
Output the K-th number to be crossed out."""
N = int(input("N: "))
K = int(input("K: "))
nums = []
crossedNums = set()
for i in range(2,N+1):
    nums.append(i)

def reseto(arr):
    c = 0
    s = 0
    p = 1
    while c < K:
        for i in range(0,len(arr)):
            if arr[0] not in crossedNums:
                print(i, " is i")
                temp = arr[0]
                break
        while temp * p <= N:
            s = temp * p
            print(crossedNums)
            crossedNums.add(arr[temp * p - 2])
            p += 1
            c += 1

    return s


print(reseto(nums))
