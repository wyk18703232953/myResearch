from functools import lru_cache
from sys import setrecursionlimit as srl

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
        ans = 1 + dp(i+1, j, A[i])
        if left >= 1:
            stack = []
            for k in range(i, j+1):
                stack.append(A[k])
                while len(stack) >= 2 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack[-1] += 1
                if len(stack) == 1 and left == stack[-1]:
                    cand = dp(k+1, j, left+1)
                    if cand < ans:
                        ans = cand
        return ans

    return dp(1, N-1, A[0])

def main(n):
    # Interpret n as the length of the array A
    # Deterministic construction of A of length n, with positive integers
    if n <= 0:
        return 0
    A = [1 + (i % 5) for i in range(n)]
    return solve(n, A)

if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    n = 10
    result = main(n)
    # print(result)
    pass