import random

def main(n: int):
    # 生成规模为 n 的测试数据，这里生成 0 到 n 之间的随机非负整数
    s = [random.randint(0, n) for _ in range(n)]

    s.sort()
    f = False
    z = s.count(0)
    p = 0

    for i in range(2, n):
        if s[i] == s[i - 1] and s[i - 1] == s[i - 2]:
            f = True

    for i in range(1, n):
        if s[i] == s[i - 1]:
            p += 1
            if i - 2 >= 0 and s[i - 2] == s[i - 1] - 1:
                f = True

    y = sum(s)
    t = n * (n - 1) // 2
    r = y - t

    if r % 2 == 0 or f or y == 0 or z >= 2 or p >= 2:
        print("cslnb")
    else:
        print("sjfnb")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)