import random
import math

def main(n: int):
    # 生成测试数据
    # k: 1~n
    # s: 1~n（避免为0）
    # p: 1~n（避免为0）
    k = random.randint(1, n)
    s = random.randint(1, n)
    p = random.randint(1, n)

    # 原逻辑
    a = n // s
    if n % s != 0:
        a += 1
    q = k * a
    m = q // p
    if q % p != 0:
        m += 1
    print(m)

if __name__ == "__main__":
    # 示例：以 n=100 作为规模运行一次
    main(100)