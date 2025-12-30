import math
import random

def main(n: int):
    # 生成规模为 n 的测试数据：
    # 原程序中只用到一个整数 n，这里我们直接使用传入的 n，
    # 如需更复杂数据，可在此处基于 n 生成额外随机数据。
    # 例如：nums = [random.randint(1, 10**6) for _ in range(n)]
    # 但后续逻辑并未使用这些数据，因此仅保留 n。

    if n == 1:
        print(1)
        return

    a = []
    for i in range(1, n + 1, 2):
        a.append(1)

    b = []
    for i in range(2, n + 1, 2):
        b.append(i)

    p = len(b)
    k = 2

    while p > 0:
        c = []
        for i in range(p):
            if b[i] % k == 0 and b[i] % (k * 2) != 0:
                a.append(k)
                p -= 1
            else:
                c.append(b[i])
        b = c[:]
        k = k * 2

    p = a[-1] // 2
    a.pop()
    q = p
    for i in range(p, n + 1):
        if i % p == 0 and i > q:
            q = i
    a.append(q)

    for i in a:
        print(i, end=" ")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)