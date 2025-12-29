import random

def main(n):
    # 随机生成测试数据：
    # 生成 n 个严格递增的灯切换时间 a[1..n]，范围在 [1, M-1]，并给定 M。
    # 保证 0 = a[0] < a[1] < ... < a[n] < M。
    #
    # 这里设定：
    #   M 与 n 同阶，M = 2*n + 2，并在 [1, M-1] 中随机选 n 个不同时间点。
    if n <= 0:
        return 0

    M = 2 * n + 2
    points = random.sample(range(1, M), n)
    points.sort()

    # 对应原代码中的输入：
    # n, M
    # a[1..n]，然后会在逻辑中被扩展为 [0] + a + [M]
    a = [0] + points + [M]

    # 下面是原 testcase() 的逻辑，但不使用 input()，而是使用上面生成的数据。
    ontime = [0] * (n + 1)
    tmp = 0
    for ind in range(n, -1, -1):
        if ind % 2 == 0:  # light will be on from now
            tmp += a[ind + 1] - a[ind]  # total ontime from ind
        ontime[ind] = tmp

    mx = ontime[0]

    # 枚举可以插入的新切换点的位置
    for ind in range(n + 1):  # iterate over segments
        l, r = a[ind], a[ind + 1]
        if r - l <= 1:
            continue
        for x in (l + 1, r - 1):
            newtime = ontime[0] - ontime[ind]
            if ind % 2 == 0:
                newtime += x - l
            else:
                newtime += r - x
            newtime += (M - r) - ontime[ind]
            mx = max(mx, newtime)

    # 输出结果
    print(mx)
    return mx

if __name__ == "__main__":
    # 示例：运行一次规模为 5 的测试
    main(5)