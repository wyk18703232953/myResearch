import random
import time
import sys


def main(n):
    """
    n: 控制测试用例规模（这里用来控制随机数种子，便于复现）
    逻辑：模拟原交互式程序，内部自建 Oracle，去掉 input()，输出最终结果。
    """

    # 保证可复现：用 n 作为随机种子的一部分
    random.seed(int(time.time()) ^ n)

    # 原程序中 bb 是随机掩码；真实的被猜测数用 x, y 表示
    # 这里我们生成测试数据 (x, y)，并据此构造交互回答函数。
    # 限制在 30 位整数范围内（与原代码一致）
    x = random.randint(0, 2 ** 30 - 1)
    y = random.randint(0, 2 ** 30 - 1)

    # 构造 Oracle：给定 (a, b) 返回比较结果
    # 原题典型逻辑：返回 sign((x^bb - a) - (y - b)) ∈ {-1, 0, 1}
    # 但原代码只用到了 0/1 两种情况，因此我们按以下方式设计：
    #   若 (x^bb) - a > (y - b) -> 返回 1
    #   若 (x^bb) - a <= (y - b) -> 返回 0
    #
    # 为了保持与原代码对 bb 的使用方式一致：
    bb = random.randint(0, 2 ** 30 - 1)

    def oracle(a, b):
        # 真实比较在 (x^bb, y) 与 (a, b) 之间
        lhs = (x ^ bb) - a
        rhs = y - b
        return 1 if lhs > rhs else 0

    # 以下是原逻辑的非交互版本：用 oracle 替代 print/input
    hat1 = 0
    hat2 = 0
    lastresult = None

    # 调试输出：说明真实答案
    print(f"# hidden x = {x}, y = {y}, bb = {bb}", file=sys.stderr)

    for i in range(29, -1, -1):
        g1 = hat1 + (1 << i)
        g2 = hat2 + (1 << i)

        if lastresult is None:
            # print('?', hat1 ^ bb, hat2)  # 原交互输出
            t1 = oracle(hat1 ^ bb, hat2)
        else:
            t1 = lastresult

        if t1 != 0:
            # print('?', g1 ^ bb, g2)
            t2 = oracle(g1 ^ bb, g2)
            if t1 != t2:
                if t1 == 1:
                    hat1 += (1 << i)
                else:
                    hat2 += (1 << i)
                lastresult = None
                continue

        lastresult = t1
        # print('?', g1 ^ bb, hat2)
        t3 = oracle(g1 ^ bb, hat2)
        if t3 == 1:
            pass
        else:
            hat1 += (1 << i)
            hat2 += (1 << i)

    # 原代码输出：print('!', hat1^bb% (2**30), hat2)
    ans1 = (hat1 ^ bb) % (2 ** 30)
    ans2 = hat2

    print(ans1, ans2)
    # 为了验证是否正确，可以在 stderr 打印对比结果
    print(f"# guess = ({ans1}, {ans2}), real = ({x}, {y})", file=sys.stderr)


if __name__ == "__main__":
    # 这里给一个默认 n，也可以在外部调用 main(n)
    main(1)