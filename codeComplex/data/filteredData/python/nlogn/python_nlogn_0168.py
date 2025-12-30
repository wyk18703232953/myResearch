import sys
from math import inf

def main(n: int):
    # 生成测试数据：n 个区间中心和长度
    # 示例：x = 0, 1, ..., n-1，w = 1
    xw = [(i, 1) for i in range(n)]

    rl = []
    for x, w in xw:
        rl.append((x - w, x + w))

    rl.sort(key=lambda x: (x[1], x[0]))

    ans = 0
    tmp = -inf

    for r, l in rl:
        if r < tmp:
            continue
        ans += 1
        tmp = l

    print(ans)


if __name__ == "__main__":
    # 示例运行：规模 n = 10
    main(10)