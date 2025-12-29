import random

def main(n):
    # 随机构造 n 组测试数据 (x, y, k)
    # 这里令 x, y, k 在 1 ~ 10^9 范围内随机生成，可按需调整
    test_cases = []
    for _ in range(n):
        x = random.randint(1, 10**9)
        y = random.randint(1, 10**9)
        k = random.randint(1, 10**9)
        test_cases.append((x, y, k))

    # 按原逻辑处理并输出结果
    for x, y, k in test_cases:
        if x > y:
            x, y = y, x
        m = y
        d = y
        if (y - x) % 2 == 1:
            d -= 1
        if k < m:
            print(-1)
            continue
        r = k - m
        if r % 2 != 0:
            r -= 1
            if d != m:
                d += 1
            else:
                d -= 1
        d += r
        print(d)


if __name__ == "__main__":
    # 示例：规模参数 n = 5
    main(5)