import random

def main(n: int):
    """
    n 为规模参数，用来控制测试数据的多样性/数量。
    这里的逻辑是：生成 3 张类似于 '1m', '9p', '3s' 的牌面字符串，
    然后运行原逻辑并打印结果。
    """
    # 花色：m=万, p=筒, s=索
    suits = ['m', 'p', 's']
    tiles = []

    # 根据 n 控制生成策略：n 越大，越偏向完全随机
    for _ in range(3):
        num = random.randint(1, min(9, max(1, n)))  # 数字 1~9，受 n 影响但不超过 9
        suit = random.choice(suits)
        tiles.append(f"{num}{suit}")

    # 原始逻辑
    line = tiles
    line.sort()
    a, b, c = line

    if a == b and a == c:
        print(0)
    elif a == b:
        print(1)
    elif b == c:
        print(1)
    else:
        if (
            a[1] == b[1]
            and b[1] == c[1]
            and int(b[0]) - int(a[0]) == 1
            and int(c[0]) - int(b[0]) == 1
        ):
            print(0)
        elif a[1] == b[1] and int(b[0]) - int(a[0]) in [1, 2]:
            print(1)
        elif b[1] == c[1] and int(c[0]) - int(b[0]) in [1, 2]:
            print(1)
        elif a[1] == c[1] and int(c[0]) - int(a[0]) in [1, 2]:
            print(1)
        else:
            print(2)


if __name__ == "__main__":
    # 示例调用：可以在外部根据需要传入不同的 n
    main(9)