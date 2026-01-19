from collections import defaultdict
from math import gcd
from heapq import heappop, heappush

def main(n):
    # Deterministically construct inputs based on n
    # n is the length of arrays A and B
    if n <= 0:
        return

    A = [i + 2 for i in range(n)]          # [2, 3, 4, ..., n+1]
    B = [i % 5 + 1 for i in range(n)]      # [1, 2, 3, 4, 5, 1, 2, ...]
    start = 0

    hp = [(0, start)]
    dis = {start: 0}
    seen = set()
    ans = -1

    while hp:
        _, x = heappop(hp)
        if x == 1:
            ans = dis[x]
            break
        if x in seen:
            continue
        seen.add(x)
        for a, b in zip(A, B):
            y = gcd(x, a)
            if y not in dis or dis[y] > dis[x] + b:
                dis[y] = dis[x] + b
                heappush(hp, (dis[y], y))

    print(ans)

if __name__ == "__main__":
    main(10)