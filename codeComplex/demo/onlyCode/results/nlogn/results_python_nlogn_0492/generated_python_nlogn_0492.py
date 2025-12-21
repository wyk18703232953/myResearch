import random
import math
import collections
import bisect

def main(n):
    m = n * 5
    space = 0
    saved = []
    for _ in range(n):
        b = random.randint(1, 10)
        extra = random.randint(0, 10)
        a = b + extra
        space += a
        saved.append(a - b)
    saved.sort(reverse=True)
    if space - sum(saved) > m:
        return -1
    count = 0
    if space <= m:
        return 0
    i = 0
    while i < n:
        count += 1
        space -= saved[i]
        if space <= m:
            return count
        i += 1

if __name__ == "__main__":
    print(main(10))