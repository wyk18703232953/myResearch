import random

def main(n: int):
    # 根据 n 生成测试数据，这里约定：
    # 1. 生成区间长度不超过 n
    # 2. l 从 1 到 n，r 从 l 到 min(l + n - 1, 2 * n) 之间
    if n <= 0:
        return

    l = random.randint(1, n)
    r = random.randint(l, min(l + n - 1, 2 * n))

    if l == r or l + 1 == r:
        print(-1)
    elif l % 2 == 0:
        print(l, l + 1, l + 2)
    elif l % 2 != 0 and r - l + 1 > 3:
        print(l + 1, l + 2, l + 3)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)