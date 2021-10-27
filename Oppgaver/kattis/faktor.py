"""
You are the editor of one scientific journal. You know how many articles you are going to publish and the owners are pushing you to reach a specific impact factor. You are wondering how many scientists you will have to bribe to cite your articles to meet the owners demands. Since money is tight you want to bribe the minimal amount of scientists. Each bribed scientist buys you a single citation.

Input
First and only line of input will contain 2 integers, A (1≤A≤100), the number of articles you plan to publish and I (1≤I≤100), the impact factor the owners require.

Output
The first and only line of output should contain one integer, the minimal number of scientists you need to bribe."""

A, I = map(int, input().split(" "))

bribe_scientists = (A * I) - A + 1

print(bribe_scientists)
