import random

def main(n):
    # 可根据需要调整测试数据生成方式
    k = random.randint(1, max(1, n))  # 保证 1 <= k <= n
    # 生成一个严格递增的数组，保证有意义的差分
    a = sorted(random.sample(range(1, 10 * n + 1), n))

    if n == 1:
        ans = 0
    else:
        diff = []
        for i in range(n - 1):
            diff.append(a[i + 1] - a[i])

        diff.sort(reverse=True)
        ans = a[-1] - a[0]
        for i in range(min(k - 1, len(diff))):
            ans -= diff[i]

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)，可按需修改 n
    main(5)