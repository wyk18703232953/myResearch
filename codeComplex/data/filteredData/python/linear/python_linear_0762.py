import random

def main(n):
    # 生成规模为 n 的测试数据
    # 约定：q 也与 n 同规模（可按需调整生成规则）
    q = n
    # 生成一个长度为 n 的数组 a，元素为 1..10^9 之间的随机整数
    # 保证有最大值以模拟原逻辑行为
    a = [random.randint(1, 10**9) for _ in range(n)]

    # ---- 原始逻辑开始（移除所有 input） ----
    M = max(a)
    i = 0
    x = a[0]
    L = []
    L1 = []
    L2 = []
    while x != M:
        L1.append(x)
        L2.append(a[i + 1])
        i = i + 1
        if x < a[i]:
            L.append(x)
            x = a[i]
        else:
            L.append(a[i])

    b = a[i + 1:] + L

    # 模拟 q 次询问：原程序中 q 行输入，每行一个 m
    # 这里用 1..(q) 的序列作为 m 值（可按需更改为随机等）
    for m in range(1, q + 1):
        if m <= i:
            print(str(L1[m - 1]) + " " + str(L2[m - 1]))
        else:
            print(str(x) + " " + str(b[(m - i - 1) % (n - 1)]))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)