import random

def main(n):
    # 生成规模为 n 的测试数据：L 中的每个元素在 [1, 100000] 之间
    max_val = 100000
    L = [random.randint(1, max_val) for _ in range(n)]

    D = [0] * 101000
    mod = 10**9 + 7
    itt = [0] * 101000
    p = [0] * 100010
    D[0] = 1

    # 预计算 2 的幂
    for i in range(100010):
        D[i + 1] = (D[i] * 2) % mod

    # 统计每个数出现次数
    for x in L:
        itt[x] += 1

    # 累加倍数上的出现次数，并计算 p[i] 的初值
    for i in range(1, max_val + 1):
        for j in range(i * 2, max_val + 1, i):
            itt[i] += itt[j]
        p[i] = (D[itt[i]] - 1) % mod

    # 反向做莫比乌斯反演形式的调整
    i = max_val
    while i >= 1:
        for j in range(i * 2, max_val + 1, i):
            p[i] -= p[j]
        p[i] %= mod
        i -= 1

    print(p[1])


if __name__ == "__main__":
    # 示例调用：规模为 10
    main(10)