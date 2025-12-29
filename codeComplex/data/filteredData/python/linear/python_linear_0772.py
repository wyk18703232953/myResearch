import random

def main(n):
    """
    n: 问题规模，用于生成测试数据。
    这里约定：
    - m = n
    - k = max(1, n // 10) 作为每页容量
    - 特殊位置 P 为 1..m 的一个随机排列的前 n 个元素再打乱
    """
    # 生成参数
    m = n
    k = max(1, n // 10)

    # 生成测试数据 P：从 1..m 中随机选取 n 个不同的数
    P = random.sample(range(1, m + 1), n)

    # ------- 原逻辑开始（移除 input()，逻辑封装在 main 中） -------
    P.reverse()

    ops = 0
    i = 1
    while P:
        nxt = P[-1]
        togo = nxt - i
        skip = togo // k * k
        i += skip

        space = k
        while space:
            special = 0
            while P and P[-1] < i + space:
                special += 1
                P.pop()
            i += space
            if not special:
                break
            ops += 1
            space = special

    print(ops)


if __name__ == "__main__":
    # 示例：以 n = 100 运行
    main(100)