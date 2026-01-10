import math
import bisect
from collections import Counter, defaultdict, deque

mod = 1000000007

def main(n):
    if n <= 0:
        return
    m = n * 2
    arr = [(i % n) + 1 for i in range(m)]
    if n > m:
        print(0)
        return
    c = Counter(arr)
    d1 = list(sorted(c.values()))
    days = 0
    for i in range(1, 101):
        d = d1.copy()
        people = 0
        done = False
        while True:
            if people >= n:
                days = i
                done = True
                break
            if len(d) == 0:
                break
            curr = d[-1] // i
            d.pop()
            people += curr
        if done:
            days = i
    print(days)

if __name__ == "__main__":
    main(1000)