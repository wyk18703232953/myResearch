import random

def main(n: int):
    # 生成测试数据
    # n: k 的长度
    # m: p 的长度，设为和 n 相同规模（可以按需调整）
    m = n

    # 生成 k 和 p，为了更有意义，生成升序整数序列
    # 你可以根据需要调整数据生成策略
    k = sorted(random.randint(1, 10 * n) for _ in range(n))
    p = sorted(random.randint(1, 10 * n) for _ in range(m))

    a = 0
    b = 0
    ans = 0
    while a != n and b != m:
        if p[b] >= k[a]:
            ans += 1
            a += 1
            b += 1
        else:
            a += 1

    print(ans)


if __name__ == "__main__":
    # 示例：n = 10
    main(10)