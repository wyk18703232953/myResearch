import random

def solve_three_tiles(a, b, c):
    if a[1] == b[1] == c[1]:
        t = sorted([int(a[0]), int(b[0]), int(c[0])])
        if (t[1] == t[0] + 1 == t[2] - 1) or (t[0] == t[2]):
            print(0)
        elif t[0] == t[1] or t[1] == t[2]:
            print(1)
        elif (t[0] + 1 == t[1] or t[1] + 1 == t[2] or
              t[0] + 2 == t[1] or t[1] + 2 == t[2]):
            print(1)
        else:
            print(2)
    elif a[1] == b[1]:
        s, t = int(a[0]), int(b[0])
        if s == t:
            print(1)
        elif min(s, t) + 1 == max(s, t) or min(s, t) + 2 == max(s, t):
            print(1)
        else:
            print(2)
    elif c[1] == b[1]:
        s, t = int(c[0]), int(b[0])
        if s == t:
            print(1)
        elif min(s, t) + 1 == max(s, t) or min(s, t) + 2 == max(s, t):
            print(1)
        else:
            print(2)
    elif a[1] == c[1]:
        s, t = int(a[0]), int(c[0])
        if s == t:
            print(1)
        elif min(s, t) + 1 == max(s, t) or min(s, t) + 2 == max(s, t):
            print(1)
        else:
            print(2)
    else:
        print(2)


def main(n):
    """
    n: 生成并测试 n 组数据，每组数据包含 3 张牌。
    牌面格式与原题一致：'<digit><char>'，例如 '1m', '9s', '3p'。
    digit 在 1~9 之间随机，char 在 'm','p','s' 中随机。
    """
    suits = ['m', 'p', 's']
    for _ in range(n):
        a = f"{random.randint(1, 9)}{random.choice(suits)}"
        b = f"{random.randint(1, 9)}{random.choice(suits)}"
        c = f"{random.randint(1, 9)}{random.choice(suits)}"
        # 如有需要查看测试数据，可打印：
        # print("Tiles:", a, b, c)
        solve_three_tiles(a, b, c)


if __name__ == "__main__":
    # 示例：运行 5 组随机测试
    main(5)