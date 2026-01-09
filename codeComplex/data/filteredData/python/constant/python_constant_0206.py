def fun(A):
    for i in range(len(A)):
        if A[i] == 0:
            return i
    return 1

def main(n):
    dp = [0] * 10
    # 生成三个正整数 k1, k2, k3，保证在 1..10 之间，且随 n 变化但确定性
    k1 = n % 10 + 1
    k2 = (2 * n) % 10 + 1
    k3 = (3 * n) % 10 + 1
    A = [k1, k2, k3]
    A.sort()
    k1, k2, k3 = A
    for i in range(0, 10, k1):
        dp[i] = 1
    for i in range(fun(dp), 10, k2):
        dp[i] = 1
    for i in range(fun(dp), 10, k3):
        dp[i] = 1
    result = (0 not in dp)
    # print("YES" if result else "NO")
    pass
if __name__ == "__main__":
    main(10)