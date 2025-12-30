import sys
from collections import defaultdict
import random

def main(n: int):
    # 生成测试数据：n 个区间 [x, y]，保证 x <= y，坐标在 [1, 2n] 范围内
    d = defaultdict(int)
    d1 = defaultdict(int)

    # 构造一些随机但合理的区间数据
    # 为了更有覆盖性，混合短区间与长区间
    coords = [i for i in range(1, 2 * n + 1)]
    for _ in range(n):
        a = random.choice(coords)
        b = random.choice(coords)
        if a > b:
            a, b = b, a
        # 原代码中的差分逻辑：对 [x, y] 进行处理
        d[a - 1] -= 1
        d[b] += 1

    if not d:
        print(" ".join("0" for _ in range(n)))
        return

    x = list(d.keys())
    x.sort()
    r = x[-1]
    c = d[r]
    temp = 1

    for i in range(len(x) - 2, -1, -1):
        l = x[i] + 1
        d1[c] += r - l + temp
        c += d[x[i]]
        r = l
        temp = 0

    # 输出从 1 到 n 的结果
    out = []
    for i in range(1, n + 1):
        out.append(str(d1[i]))
    print(" ".join(out))


if __name__ == "__main__":
    # 示例：运行规模 n=5
    main(5)