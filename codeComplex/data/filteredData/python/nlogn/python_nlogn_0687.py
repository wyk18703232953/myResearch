import random

def main(n):
    # 生成规模为 n 的测试数据
    # 约定：b 长度为 n，g 长度为 n（可按需要修改）
    m = n

    # 生成保证可行的随机数据：max(b) <= min(g)
    # 先生成 b
    b = [random.randint(1, 100) for _ in range(n)]
    b.sort()
    # 确保 g 的最小值 >= b 的最大值
    base = b[-1]
    g = [random.randint(base, base + 100) for _ in range(m)]
    g.sort()

    # 以下为原逻辑
    if b[-1] > g[0]:
        print(-1)
        return

    a = 0
    a += sum(g) - g[0]
    if g[0] == b[-1]:
        a += g[0]
        a += m * sum(b[:-1])
        print(a)
    else:
        a += g[0]
        if n >= 2:
            a += m * sum(b[:-2]) + (m - 1) * b[-2] + b[-1]
        else:
            # 当 n=1 时，没有 b[:-2] 和 b[-2]，根据原意退化处理
            # 这里等价于所有 g 的值都 >= b[0]，且 g[0] > b[0]
            a += b[0]
        print(a)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)