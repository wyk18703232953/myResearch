import random

def main(n):
    # 生成测试数据：
    # n：任务数量
    # 对每个任务生成：
    #   i：任务的最低要求数量，范围 [1, n]
    #   j：任务的耗时，范围 [1, n]
    # 同时生成总时间 T，使得平均上可以选到若干任务
    #
    # 注：原代码输入格式为：
    # n T
    # (重复 n 行/或一行) 每个任务: i j
    #
    # 这里按相同逻辑在内存中构造这些数据
    T = n * 5  # 可根据需要调整 T 的规模
    tasks = []
    for idx in range(1, n + 1):
        i = random.randint(1, n)
        j = random.randint(1, n)
        # 原代码中的 a 元素为 (index, i, j)，且以 j 排序
        tasks.append((idx, i, j))

    # 按耗时 j 升序排序
    a = sorted(tasks, key=lambda x: x[-1])

    be, en, ans = 0, n, []

    # 二分出最大的可行 md
    while be < en:
        md = (be + en + 1) >> 1
        time = 0
        c = 0

        for _, i, j in a:
            if time + j <= T and i >= md:
                time += j
                c += 1

        if c >= md:
            be = md
        else:
            en = md - 1

    l = be
    for _, i, j in a:
        if be and i >= l:
            ans.append(_)
            be -= 1

    # 保持与原程序一致的输出格式
    print(f"{l}\n{l}")
    print(*ans)


# 示例运行：可在本文件直接测试
if __name__ == "__main__":
    main(10)