import random

def main(n):
    # 生成 n 组测试数据 (l, r)，保证 l <= r
    test_cases = []
    for _ in range(n):
        l = random.randint(-10**6, 10**6)
        r = random.randint(l, l + random.randint(0, 10**6))
        test_cases.append((l, r))

    for l, r in test_cases:
        if (l - r) % 2 == 1:
            if l % 2:
                print((r - l + 1) // 2)
            else:
                print(-((r - l + 1) // 2))
        else:
            ans = 0
            if l % 2:
                ans = ans + (r - l) // 2
            else:
                ans = ans - (r - l) // 2
            if r % 2:
                ans = ans - r
            else:
                ans = ans + r
            print(ans)


if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)