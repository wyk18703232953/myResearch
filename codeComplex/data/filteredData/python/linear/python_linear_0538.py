import sys
import random

def main(n: int):
    # 生成规模为 n 的测试数据：整数列表 za
    # 这里示例生成范围在 [-10^6, 10^6] 的随机整数
    random.seed(0)
    za = [random.randint(-10**6, 10**6) for _ in range(n)]

    # 以下是原逻辑，移除了 input()：
    N = n

    if N == 1:
        print(za[0])
        return

    t1 = max(za)
    t2 = min(za)
    if t2 >= 0:
        print(sum(za) - 2 * t2)
        return
    if t1 <= 0:
        print(2 * t1 - sum(za))
        return

    res = 0
    for x in za:
        res += abs(x)

    print(res)


if __name__ == "__main__":
    # 示例：调用 main，规模可自行修改
    main(5)