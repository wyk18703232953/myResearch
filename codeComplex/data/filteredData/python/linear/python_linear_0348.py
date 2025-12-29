import math
import random

def main(n):
    # 根据 n 生成测试数据
    # 随机生成 k（区间数量），这里设为 0 到 n 之间
    k = random.randint(0, n)

    # 随机生成 k 个区间 (l, r)，1 <= l <= r <= n
    intervals = []
    for _ in range(k):
        l = random.randint(1, n)
        r = random.randint(l, n)
        intervals.append((l, r))

    # 原逻辑中实际上并未使用这些区间，仅仅读入
    # 保持与原逻辑一致，仅根据 n 输出 1010... 交替串

    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append('0')
        else:
            result.append('1')

    print(''.join(result))

if __name__ == "__main__":
    # 示例：调用 main(10)，真实使用时可以在此处修改 n
    main(10)