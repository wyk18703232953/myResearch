import random

def main(n: int):
    """
    n: 规模，表示测试数据组数 cs
    随机生成 n 组 (l, r)，l <= r，范围可按需调整
    """
    cs = n
    # 生成测试数据：这里设定 l, r 在 [-10^6, 10^6] 范围内
    test_cases = []
    for _ in range(cs):
        a = random.randint(-10**6, 10**6)
        b = random.randint(-10**6, 10**6)
        l, r = (a, b) if a <= b else (b, a)
        test_cases.append((l, r))

    for l, r in test_cases:
        if l % 2 == 0 and r % 2 == 0:
            print((r - l) // 2 + l)
        if l % 2 == 1 and r % 2 == 0:
            print((r - l + 1) // 2)
        if l % 2 == 0 and r % 2 == 1:
            print(-(r - l + 1) // 2)
        if l % 2 == 1 and r % 2 == 1:
            print(-(r - l) // 2 - l)


if __name__ == "__main__":
    # 示例：运行 5 组测试
    main(5)