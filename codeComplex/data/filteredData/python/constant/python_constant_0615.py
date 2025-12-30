import random

def main(n):
    # 生成 n 组测试数据 (a, b)，范围可按需调整
    test_cases = []
    for _ in range(n):
        a = random.randint(-10**5, 10**5)
        b = random.randint(-10**5, 10**5)
        # 保证 a <= b，便于和原逻辑对比
        if a > b:
            a, b = b, a
        test_cases.append((a, b))

    for a, b in test_cases:
        a1 = a
        if a % 2 == 0:
            a1 += 1
        b1 = b
        if b % 2 == 0:
            b1 -= 1
        res1 = 0
        if a1 <= b1:
            num = (b1 - a1) // 2 + 1
            res1 = num * (b1 + a1) // 2
            res1 *= -1

        b2 = b
        a2 = a
        if a % 2 == 1:
            a2 += 1
        if b % 2 == 1:
            b2 -= 1
        res2 = 0
        if a2 <= b2:
            num = (b2 - a2) // 2 + 1
            res2 = num * (b2 + a2) // 2

        print(res1 + res2)


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)