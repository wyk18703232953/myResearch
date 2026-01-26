from collections import defaultdict, Counter, deque
from math import sqrt, log10, log, floor, factorial, gcd
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations

inf = float('inf')
mod = 10 ** 9 + 7
def yn(a): print("YES" if a else "NO")
ceil = lambda a, b: (a + b - 1) // b

lim = 22
po = [1 << j for j in range(lim + 1)]
maxbits = lim
masks = po[lim]
dp = [-1] * masks

def main(n):
    global dp
    dp = [-1] * masks

    # 生成确定性输入列表 l，元素范围限制在 [0, masks-1]
    # 为了覆盖更多位模式，使用简单的算术构造
    l = [i % masks for i in range(n)]

    for x in l:
        dp[x] = x
    for i in range(masks):
        for j in range(maxbits):
            if dp[i] == -1 and (i & (1 << j)):
                dp[i] = dp[i - (1 << j)]
    ans = [dp[x ^ (masks - 1)] for x in l]
    print(*ans)

if __name__ == "__main__":
    main(10)