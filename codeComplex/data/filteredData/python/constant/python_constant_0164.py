import random

def main(n: int):
    # 依据规模 n 生成测试数据：构造一个区间 [l, r]，长度为 n
    # 这里让 l 随机，r = l + n - 1
    # 你也可以改成固定 l，例如 l = 1
    l = random.randint(1, 100)
    r = l + n - 1

    j = r - l + 1  # 区间长度

    if j == 3:
        if l % 2 == 0:
            print(l, l + 1, l + 2)
        else:
            print(-1)
    elif j > 3:
        if l % 2 == 0:
            print(l, l + 1, l + 2)
        else:
            print(l + 1, l + 2, l + 3)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)