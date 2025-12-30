import random

def main(n):
    # 1. 生成测试数据
    # 规模 n：我们令 B 长度为 n，G 长度为 n（或可按需调整）
    m = n

    # 生成 B 和 G，保证 min(G) >= max(B) 的概率较大，以避免总是输出 -1
    B = [random.randint(1, 100) for _ in range(n)]
    z = max(B)
    # 让 G 的元素大部分不小于 z
    G = [random.randint(z, z + 100) for _ in range(m)]

    # 2. 原逻辑开始
    if min(G) < max(B):
        print(-1)
        return

    cnt = 0
    z = max(B)
    y = 0
    f = 1
    f2 = 0

    for i in B:
        if i != z or f2:
            y = max(y, i)
        else:
            f2 = 1

    for i in G:
        if i == z:
            f = 0
        cnt += i - z

    if f:
        cnt += z - y

    print(cnt + sum(B) * m)

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)