import random

def main(n):
    # 生成测试数据
    # n: 数组长度
    # m: 取 1 和 2 的标记数量，设为 n
    m = n

    # ar: 随机整数数组
    # 元素范围可以根据需要调整，这里设为 -10^6 到 10^6
    ar = [random.randint(-10**6, 10**6) for _ in range(n)]

    # flags: 由 1 和 2 组成的数组，长度为 m (=n)
    # 保证至少有一个 1，以避免原算法中 art 为空导致的问题
    if n == 1:
        flags = [1]
    else:
        # 随机生成，然后强制至少一个 1
        flags = [random.choice([1, 2]) for _ in range(n)]
        if all(f != 1 for f in flags):
            pos = random.randrange(n)
            flags[pos] = 1

    # 以下为原始逻辑的无 input() 封装实现
    arc = []
    art = []
    res = []
    for idx, val in enumerate(flags):
        if val == 1:
            art.append(ar[idx])
            res.append(0)
        else:
            arc.append(ar[idx])

    nt = 0
    for i in arc:
        while nt != len(art) - 1 and abs(art[nt] - i) > abs(art[nt + 1] - i):
            nt += 1
        res[nt] += 1

    # 输出结果（与原程序一致）
    print(" ".join(str(x) for x in res))


if __name__ == "__main__":
    # 示例：n = 10，可按需修改或由外部调用 main(n)
    main(10)