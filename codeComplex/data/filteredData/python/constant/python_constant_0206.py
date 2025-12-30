import random

def fun(A):
    for i in range(len(A)):
        if A[i] == 0:
            return i
    return 1

def Y(c):
    print(["NO", "YES"][c])

def main(n):
    # n 作为规模参数，用来生成测试数据
    # 原程序只需要三个整数 k1, k2, k3，取值在 1~9 且互不相同
    # 这里根据 n 固定一个可重复的随机种子，保证同一 n 生成的数据一致
    random.seed(n)
    k1, k2, k3 = random.sample(range(1, 10), 3)

    dp = [0] * 10
    # 按原逻辑排序（虽然 random.sample 已经是无序的，但保持一致）
    A = sorted([k1, k2, k3])
    k1, k2, k3 = A

    for i in range(0, 10, k1):
        dp[i] = 1
    for i in range(fun(dp), 10, k2):
        dp[i] = 1
    for i in range(fun(dp), 10, k3):
        dp[i] = 1

    Y(0 not in dp)

if __name__ == "__main__":
    # 示例：使用 n=1 运行
    main(1)