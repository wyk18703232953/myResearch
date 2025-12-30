from math import log2, ceil
from collections import deque, Counter as CC, defaultdict as dd
import random


class union_find:
    def __init__(self, n):
        self.n = n
        self.rank = [0] * n
        self.parent = [int(j) for j in range(n)]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if self.rank[i] == self.rank[j]:
            self.parent[i] = j
            self.rank[j] += 1
        elif self.rank[i] > self.rank[j]:
            self.parent[j] = i
        else:
            self.parent[i] = j

    def find(self, i):
        temp = i
        if self.parent[temp] != temp:
            self.parent[temp] = self.find(self.parent[temp])
        return self.parent[temp]


def solve(p, q, r, a, b, c):
    a.sort()
    b.sort()
    c.sort()
    l = [a, b, c]

    dp = [[[0 for _ in range(r + 1)] for _ in range(q + 1)] for _ in range(p + 1)]
    for i in range(p + 1):
        for j in range(q + 1):
            for k in range(r + 1):
                s = [i - 1, j - 1, k - 1]
                for u in range(3):
                    s[u] += 1
                    try:
                        tmp = dp[s[0]][s[1]][s[2]]
                    except IndexError:
                        s[u] -= 1
                        continue
                    tmp2 = 1
                    flag = True
                    for t in range(3):
                        if u != t:
                            if s[t] == -1:
                                flag = False
                                break
                            tmp2 *= l[t][s[t]]
                    tmp += tmp2
                    s[u] -= 1
                    if flag:
                        dp[i][j][k] = max(dp[i][j][k], tmp)
    return dp[p][q][r]


def main(n):
    # 使用 n 作为规模参数，生成 p, q, r 以及数组长度
    # 这里简单设定：p = q = r = min(3, n)，数组长度分别为 p, q, r
    p = q = r = min(3, n)

    # 生成测试数据：随机正整数，范围 1..n
    a = [random.randint(1, n) for _ in range(p)]
    b = [random.randint(1, n) for _ in range(q)]
    c = [random.randint(1, n) for _ in range(r)]

    ans = solve(p, q, r, a, b, c)
    print(ans)


if __name__ == "__main__":
    # 示例：可修改 n 测试
    main(5)