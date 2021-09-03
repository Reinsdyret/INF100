"""
Jessica has a couple of steel rods next to her bed – as one does – 
and decides to go to the blacksmith apprentice Jack to get him to fuse them together.

The good thing about Jack is that he’ll fuse the steel rods together for free. 
But Jack isn’t that good at fusing things together. When fusing two rods, 
the fused rod will lose 1

cm of their combined length.

That’s not a problem for Jessica, 
but she wonders how big her javelin will become if Jack fuses all the rods together.
Input

The first line consist of an integer N
, the number of steel rods she has. Then follows N lines, each containing a single integer L(i)

representing the length of the steel rod in cm.
Output

Print out the length of the jumbo javelin Jack has made for her.
"""
import sys

N = int(sys.stdin.readline())
rods = []

for i in range(N):
    rods.append(int(sys.stdin.readline()))

sys.stdout.write(str(sum(rods) - (N-1)))
