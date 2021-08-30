"""
Input
The first line of input contains two integers n (1≤n≤10) and k (0≤k≤n), where n is the total number of judges, and k is the number of judges who have already rated the problem.

Each of the next k lines contains a single integer r (−3≤r≤3). These are the ratings of the k judges that have already rated the problem.

Output
Output two space-separated floating point numbers on a single line, 
which are the minimum and maximum overall rating the problem could achieve after the remaining judges rate the problem, minimum first. 
These values must be accurate to an absolute or relative error of 10−4."""

n, k = input().split()
n = int(n)
k = int(k)
ratings = []
sumRatings = 0
lowest = 0
highest = 0
for i in range(0,k):
    ratings.append(float(input()))
    sumRatings += ratings[i]

d = n - k
if d != 0:
    lowest = ((sumRatings + (-3 * d))) / (len(ratings) + d)
    highest = ((sumRatings + (3 * d))) / (len(ratings) + d)
    print(lowest, highest)
else:
    print(sumRatings/len(ratings),sumRatings/len(ratings))