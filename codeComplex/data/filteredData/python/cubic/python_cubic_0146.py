from functools import lru_cache
from sys import setrecursionlimit as srl
import random

srl(10**5)

def solve(N, A):
    @lru_cache(None)
    def dp(i, j, left=0):
        if i == j:
            if left == 0:
                return 1
            if A[i] == left:
                return 1
            return 2
        if i > j:
            return 0 if left == 0 else 1
        ans = 1 + dp(i + 1, j, A[i])
        if left >= 1:
            stack = []
            for k in range(i, j + 1):
                stack.append(A[k])
                while len(stack) >= 2 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack[-1] += 1
                if len(stack) == 1 and left == stack[-1]:
                    cand = dp(k + 1, j, left + 1)
                    if cand < ans:
                        ans = cand
        return ans

    # 原始调用是 dp(1, N-1, A[0])，索引从 0 开始
    return dp(1, N - 1, A[0])

def main(n):
    random.seed(0)
    # 根据 n 生成测试数据（与原注释中示例一致，取值范围 1~5）
    A = [random.randint(1, 5) for _ in range(n)]
    # 原 solve 中 N 是数组长度
    ans = solve(n, A)
    print(ans)

if __name__ == "__main__":
    # 示例：运行规模 n=500，可自行修改
    main(500)