import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里生成一个长度为 n 的区间 [l, r]
    # l 从 1 到 10n 之间随机选择，r = l + n
    l = random.randint(1, 10 * n)
    r = l + n

    if (l % 2 == 0 and r - l > 1):
        print(l, l + 1, l + 2, end=" ")
    elif (l % 2 != 0 and r - l > 2):
        print(l + 1, l + 2, l + 3, end=" ")
    else:
        print("-1")


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(10)