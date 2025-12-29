import random

def main(n: int):
    # 生成测试数据
    # 令 m = n，k 为 1 到 n 之间的随机值
    m = n
    k = random.randint(1, max(1, n))
    # 生成 1..n 的随机排列作为 p
    p = list(range(1, n + 1))
    random.shuffle(p)
    p = tuple(p)

    # 原逻辑
    d = 0
    part = (p[0] - 1) // k
    moves = 0
    skip = 0

    for pi in p:
        if (pi - 1 - d) // k == part:
            skip += 1
            continue
        d += skip
        part = (pi - 1 - d) // k
        skip = 1
        moves += 1

    print(moves + 1)


if __name__ == "__main__":
    # 示例：可根据需要修改 n
    main(10)