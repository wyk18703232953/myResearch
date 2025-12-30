import random

def main(n):
    """
    n: 规模参数，用于生成测试数据
    生成方式示例：
      m = n
      总长度 n2 = n + m = 2n
      在 ti 中放置 m 个 1 和 n 个 0 的随机排列
      对应长度生成 xi
    """
    # 1. 根据 n 生成测试数据
    m = n
    n2 = n + m

    # 构造 ti：m 个 1，n 个 0，然后打乱
    ti = [1] * m + [0] * n
    random.shuffle(ti)

    # 构造 xi：这里简单用 1..n2 的随机排列，或可改为其他分布
    xi = list(range(1, n2 + 1))
    random.shuffle(xi)

    # 2. 原逻辑
    ai = [0] * (m + 2)
    ar = [0] * (m + 2)
    ar[-1] = 10**11
    ar[0] = -10**11

    j = 1
    for i in range(n2):
        if ti[i] == 1:
            ar[j] = xi[i]
            j += 1

    i1 = 0
    i2 = 1
    for i in range(n2):
        if ti[i] == 1:
            i2 += 1
            i1 += 1
            continue
        num = xi[i] - ar[i1]
        num2 = ar[i2] - xi[i]
        if num <= num2:
            ai[i1] += 1
        else:
            ai[i2] += 1

    # 3. 输出结果（行为与原程序一致）
    for i in range(1, m + 1):
        print(ai[i], end=" ")
    print()


if __name__ == "__main__":
    # 示例：可自行修改 n
    main(5)