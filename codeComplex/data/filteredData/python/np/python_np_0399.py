import random

def main(n):
    # 随机生成 m（特征维度）
    m = random.randint(1, min(10, max(1, n)))  # 控制 m 不要过大，避免 2^m 过大
    mask = (1 << m) - 1

    # 生成测试数据矩阵 l：n 行 m 列，每个元素是 [0, 10^9] 的整数
    l = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    lo = -1  # Possible
    hi = 10 ** 9 + 1  # Impossible

    outi, outj = 0, 0  # 预先定义，避免逻辑异常时未定义

    while hi - lo > 1:
        test = (hi + lo) // 2

        things = dict()
        for i in range(n):
            curr = 0
            for v in l[i]:
                curr <<= 1
                if v >= test:
                    curr |= 1
            things[curr] = i

        works = False
        for v1 in things:
            for v2 in things:
                if (v1 | v2) == mask:
                    outi = things[v1]
                    outj = things[v2]
                    works = True
                    break
            if works:
                break

        if works:
            lo = test
        else:
            hi = test

    # 输出 1-based 索引
    print(outi + 1, outj + 1)


if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)