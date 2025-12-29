import random

def main(n: int):
    # 生成测试数据
    # p, l, r 都在 [1, n] 范围内，且 l <= r
    p = random.randint(1, n)
    l = random.randint(1, n)
    r = random.randint(l, n)

    if l == 1 and r == n:
        print(0)
    elif l == 1:
        print(abs(p - r) + 1)
    elif r == n:
        print(abs(p - l) + 1)
    else:
        print(min(abs(p - l), abs(p - r)) + r - l + 2)


if __name__ == "__main__":
    # 示例：调用 main，n 为问题规模
    main(10)