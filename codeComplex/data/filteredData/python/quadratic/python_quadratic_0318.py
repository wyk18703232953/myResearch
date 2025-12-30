import random

def main(n: int):
    # 生成测试数据：长度为 n 的数组和窗口最大长度 k
    # 示例策略：元素在 [-1000, 1000] 范围内，k 在 [1, n] 内随机选择
    if n <= 0:
        return

    k = random.randint(1, n)
    arr = [random.randint(-1000, 1000) for _ in range(n)]

    rsum = [0]
    maxx = 0.0

    # 前缀和
    for i in range(n):
        rsum.append(rsum[-1] + arr[i])

    # 枚举长度为 ki 的连续子数组，计算其平均值，并维护最大平均值
    for ki in range(k, n + 1):
        for i in range(n - ki + 1):
            avg = (rsum[i + ki] - rsum[i]) / ki
            if avg > maxx:
                maxx = avg

    print(maxx)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可修改 n
    main(10)