import random

def main(n):
    # 规模 n 用来控制测试数据的范围，这里假设：
    # 1 <= a, s <= n
    # q 至少要不小于 a 和 s，且不超过 2n
    a = random.randint(1, n)
    s = random.randint(1, n)
    q = random.randint(max(a, s), 2 * n)

    if (a + s - 2) <= (q + q - a - s):
        print("White")
    else:
        print("Black")


if __name__ == "__main__":
    # 可在此处修改 n 的大小以生成不同规模的测试数据
    main(10)