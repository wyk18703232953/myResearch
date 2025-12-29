from collections import namedtuple
import random

HS = namedtuple('HS', 'x1 x2 y')

def main(n):
    # 生成测试数据
    # n: 竖线数量
    # m: 横线数量，这里设为 n 的同数量级，可按需调整
    m = n

    # 生成竖线位置 vs：随机 1..1e9 之间的整数
    vs = [random.randint(1, 10**9) for _ in range(n)]

    # 生成横线 hs:
    # 其中一部分为 x1=1,x2=1e9 的“全宽”线段
    # 另一部分为 x1=1,x2<1e9 的线段
    hs = []
    for _ in range(m):
        x1 = 1
        # 约一半为覆盖全宽的线段
        if random.random() < 0.5:
            x2 = 10**9
        else:
            x2 = random.randint(1, 10**9 - 1)
        y = random.randint(1, 10**9)
        hs.append(HS(x1, x2, y))

    # 原始逻辑开始
    vs.sort()

    hr = len([s for s in hs if s.x1 == 1 and s.x2 == 10**9])
    hs2 = [s.x2 for s in hs if s.x1 == 1 and s.x2 < 10**9]
    hs2.sort()

    r = hc = len(hs2)
    vi = 0
    for hi in range(hc):
        while vi < n and hs2[hi] >= vs[vi]:
            vi += 1
        c = (hc - hi - 1) + vi
        if c < r:
            r = c

    result = r + hr
    print(result)
    return result

if __name__ == "__main__":
    # 示例：规模 n=10
    main(10)