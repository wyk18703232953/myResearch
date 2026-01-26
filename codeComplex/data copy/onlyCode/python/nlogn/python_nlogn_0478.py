import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
from collections import Counter
from collections import defaultdict as dd
from collections import deque

# sys.setrecursionlimit(100000000)

flush = lambda: stdout.flush()
stdstr = lambda: stdin.readline()
stdint = lambda: int(stdin.readline())
stdpr = lambda x: stdout.write(str(x))
stdmap = lambda: map(int, stdstr().split())
stdarr = lambda: list(map(int, stdstr().split()))

mod = 1000000007


n,m = stdmap()
arr =  stdarr()

if(n > m):
    print(0)
else:
    c = Counter(arr)
    d1 = list(sorted(c.values()))

    days = 0
    for i in range(1, 101):
        br = False
        d = d1.copy()

        people = 0
        done = False

        while(1):
            if(people >= n):
                # print(people, i, d[-1])
                days = i
                done = True
                break
            else:
                if(len(d) == 0):
                    break
                curr = d[-1]//i


                d.pop()


                people += curr

        if(done):
            days = i

    print(days)