import random

def main(n: int):
    # 1. 生成测试数据
    # 生成一个长度为 n 的数组 A，元素为随机整数
    A = [random.randint(-10**6, 10**6) for _ in range(n)]
    # 生成 k，保证 1 <= k <= n
    k = random.randint(1, n)

    # 2. 原始逻辑
    B = []
    for i in range(n - 1):
        B.append([A[i + 1] - A[i], i])
    B.sort(reverse=True)

    C = []
    for i in range(k - 1):
        C.append(B[i][1])
    C.sort()

    ans = 0
    mi = 10 ** 9
    ma = -10 ** 9
    u = 0
    for i in range(n):
        mi = min(mi, A[i])
        ma = max(ma, A[i])
        if u < len(C) and i == C[u]:
            ans += ma - mi
            mi = 10 ** 9
            ma = -10 ** 9
            u += 1

    result = ans + ma - mi

    # 输出结果，若需要也可一并输出生成的测试数据
    print("n =", n)
    print("k =", k)
    print("A =", A)
    print("answer =", result)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需修改
    main(10)