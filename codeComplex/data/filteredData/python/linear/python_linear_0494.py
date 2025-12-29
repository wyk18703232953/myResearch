import random
import sys

def solve(a):
    n = len(a)
    if n == 1:
        return [1]

    dp = [[-1 for _ in range(5)] for _ in range(n)]

    # i = 1 (second element), base transitions without dp check
    for i in range(1, min(2, n)):
        if a[i] < a[i - 1]:
            for j in range(5):
                ch = -1
                for k in range(5):
                    if k > j:
                        ch = k
                dp[i][j] = ch
        elif a[i] > a[i - 1]:
            for j in range(5):
                ch = -1
                for k in range(5):
                    if k < j:
                        ch = k
                dp[i][j] = ch
        else:
            for j in range(5):
                ch = -1
                for k in range(5):
                    if k != j:
                        ch = k
                dp[i][j] = ch

    # i >= 2 transitions with dp[i-1][k] validity check
    for i in range(2, n):
        if a[i] < a[i - 1]:
            for j in range(5):
                ch = -1
                for k in range(5):
                    if k > j and dp[i - 1][k] != -1:
                        ch = k
                dp[i][j] = ch
        elif a[i] > a[i - 1]:
            for j in range(5):
                ch = -1
                for k in range(5):
                    if k < j and dp[i - 1][k] != -1:
                        ch = k
                dp[i][j] = ch
        else:
            for j in range(5):
                ch = -1
                for k in range(5):
                    if k != j and dp[i - 1][k] != -1:
                        ch = k
                dp[i][j] = ch

    ind = -1
    for i in range(5):
        if dp[-1][i] != -1:
            ind = i

    if ind == -1:
        return [-1]

    res = [ind + 1]
    for i in range(n - 1, 0, -1):
        res.append(dp[i][ind] + 1)
        ind = dp[i][ind]
    res.reverse()
    return res

def main(n):
    # 生成规模为 n 的测试数据：数组元素在 [1, 10^9] 范围内
    random.seed(0)
    a = [random.randint(1, 10**9) for _ in range(n)]
    ans = solve(a)
    print(*ans)

if __name__ == "__main__":
    # 示例：可以修改这里的 n 以运行不同规模
    main(10)