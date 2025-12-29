from collections import defaultdict
import random

def main(n):
    # 生成测试数据：长度为 n 的数组 p，以及一个存在于 p 中的 m
    if n <= 0:
        return 0

    # 生成一个随机数组 p，元素值范围可自行调整
    p = [random.randint(1, 10) for _ in range(n)]
    # 确保 m 在 p 中出现
    m = p[random.randrange(n)]

    x = [0] * (n + 1)
    l = 0  # l 为 m 所在位置（最后一次出现的位置）
    for i in range(n):
        if p[i] < m:
            x[i + 1] = -1
        elif p[i] > m:
            x[i + 1] = 1
        else:
            l = i
    for i in range(1, n + 1):
        x[i] += x[i - 1]

    cnt = [defaultdict(lambda: 0) for _ in range(2)]
    for i in range(l + 1):
        cnt[i % 2][x[i]] += 1

    ans = 0
    for i in range(l + 1, n + 1):
        xi = x[i]
        ans += cnt[i % 2][xi - 1]
        ans += cnt[(i % 2) ^ 1][xi]

    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：调用 main(n) 运行
    main(10)