from math import log
from collections import deque
import random

def main(n):
    k = max(1, n)
    s = [random.randint(1, 10**9) for _ in range(n)]
    ans = 0
    s.sort()
    s1 = deque(s)
    for j in range(11):
        d = dict()
        z = 10**j
        for i in s:
            y = i * z
            u = y % k
            if u in d:
                d[u] += 1
            else:
                d.update({u: 1})
        aux = 0
        for i in s1:
            y = i
            lg = int(log(i, 10)) + 1
            lg = 10**lg
            if lg == z:
                d[(y * z) % k] -= 1
                x = (k - y % k)
                if y % k == 0:
                    x = 0
                if x in d:
                    ans += d[x]
                d[(y * z) % k] += 1
                aux += 1
            else:
                break
        for _ in range(aux):
            s1.popleft()
    return ans

if __name__ == "__main__":
    print(main(10))