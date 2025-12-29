# Legends Always Come Up with Solution
# Converted to parameterized main(n) with generated test data

from heapq import heappush, heappop
import random

def main(n):
    # 1. Generate test data based on scale n
    # You can adjust ranges as needed
    x = random.randint(1, 10**6)
    y = random.randint(1, 10**6)

    # Generate n intervals [u, v] with u <= v
    a, b = [], []
    for _ in range(n):
        u = random.randint(0, 10**6)
        v = random.randint(u, u + random.randint(0, 10**6))
        a.append((u, 1))
        a.append((v, -1))

    # 2. Original logic (no input())
    a.sort(key=lambda x: x[0] * 10000000000 - x[1])
    mod = 10**9 + 7
    t, z, ans = 1, 1, x
    for i in range(1, len(a)):
        z += a[i][1]
        if z < t:
            ans = (ans + t * (a[i][0] - a[i-1][0]) * y) % mod
            heappush(b, -a[i][0])
        else:
            if b:
                if x < (a[i][0] + b[0]) * y:
                    ans = (ans + t * (a[i][0] - a[i-1][0]) * y + x) % mod
                else:
                    ans = (ans + t * (a[i][0] - a[i-1][0]) * y + (a[i][0] + b[0]) * y) % mod
                    heappop(b)
            else:
                ans = (ans + t * (a[i][0] - a[i-1][0]) * y + x) % mod
        t = z

    print(ans)
    return ans

# Example call:
# main(5)