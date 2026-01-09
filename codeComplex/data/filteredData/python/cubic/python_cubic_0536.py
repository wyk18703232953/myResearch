from collections import defaultdict
from collections import Counter
from collections import deque
import heapq

inf = float('inf')
ninf = float('-inf')

M1 = 10**9 + 7
M2 = 998244353

def pre():
    "Start"

def solve(a: str, b: str):
    n = len(a)
    if len(a) < len(b):
        a_sorted = sorted(list(a), reverse=True)
        return "".join(a_sorted)
    b_int = int(b)
    ans = 0
    cnt = [0] * 10
    for i in range(n):
        cnt[ord(a[i]) - ord('0')] += 1

    def getrem(k):
        cnt[k] -= 1
        res = ""
        for d in range(10):
            if cnt[d] > 0:
                res += str(d) * cnt[d]
        cnt[k] += 1
        return res

    prev = ""
    for i in range(n):
        for j in range(9, -1, -1):
            if cnt[j] > 0:
                newval = prev + str(j) + getrem(j)
                if int(newval) <= b_int:
                    ans = max(ans, int(newval))
                    prev += str(j)
                    cnt[j] -= 1
                    break
    return ans

def generate_input(n: int):
    # n controls the length of string a
    # a: digits from 0..9 cycling, length n
    a = "".join(str(i % 10) for i in range(n))
    # b: an integer string of same length n, constructed deterministically
    # make b relatively large but comparable: pattern 9876543210 repeating
    pattern = "9876543210"
    b = (pattern * ((n + len(pattern) - 1) // len(pattern)))[:n]
    return a, b

def main(n):
    pre()
    a, b = generate_input(n)
    result = solve(a, b)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)