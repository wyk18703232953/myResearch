import random

def main(n):
    # 生成 n 组测试数据 (l, r)，保证 1 <= l <= r <= 2n 或任意可调范围
    test_cases = []
    for _ in range(n):
        l = random.randint(1, 2 * n)
        r = random.randint(l, 2 * n)
        test_cases.append((l, r))

    # 处理逻辑（与原代码一致）
    for l, r in test_cases:
        l -= 1
        sr = r // 2 + (r % 2) * -r
        sl = l // 2 + (l % 2) * -l
        print(sr - sl)


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)