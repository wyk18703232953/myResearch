import math
from functools import lru_cache

def main(n):
    # n controls both number of pairs and k
    if n <= 0:
        return
    # Generate deterministic k in range [1, n]
    k = n // 2 + 1 if n > 1 else 1

    # Generate deterministic array of (x, y) pairs
    arr = []
    for i in range(n):
        x = i // 2
        y = n - i
        arr.append((x, y))
        arr.sort(key=lambda x: (x[0], -x[1]), reverse=True)

    req = arr[k - 1]
    count = 0
    for a in arr:
        if a == req:
            count += 1
    print(count)

if __name__ == "__main__":
    main(10)