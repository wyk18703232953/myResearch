# Problem Link: https://codeforces.com/problemset/problem/257/A
# Author: Raunak Sett
import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

# do magic here

n, m, k = map(int, input().split())

# Sort filters
filters = list(map(int, input().split()))
filters.sort()

supply_filters_needed = 0
if k < m:
    spots = k
    end = n - 1
    while spots < m and end >= 0:
        spots += filters[end] - 1
        supply_filters_needed += 1
        end -= 1

    if spots < m:
        print(-1)
    else:
        print(supply_filters_needed)
else:
    print(0)    