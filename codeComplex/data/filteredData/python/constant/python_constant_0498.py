import random

def main(n):
    # 生成 n 组测试数据，每组 (a, b, k)
    # 这里假设 a, b, k 范围在 0~10^9，可按需调整
    test_cases = []
    for _ in range(n):
        a = random.randint(0, 10**9)
        b = random.randint(0, 10**9)
        k = random.randint(0, 10**9)
        test_cases.append((a, b, k))

    # 处理并输出结果
    for a, b, k in test_cases:
        if a < b:
            a, b = b, a
        if a > k:
            print(-1)
        elif a % 2 == b % 2 != k % 2:
            print(k - 2)
        elif (a + b) % 2 != 0:
            print(k - 1)
        else:
            print(k)


if __name__ == "__main__":
    # 示例：运行规模为 5
    main(5)