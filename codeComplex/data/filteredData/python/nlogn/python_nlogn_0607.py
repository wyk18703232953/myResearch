def main(n):
    # n 表示数组长度
    if n <= 0:
        return 0

    # 确定性生成 n 和 k
    N = n
    K = max(1, n // 2)

    # 确定性生成数组 a，元素为正整数
    # 保证有一定重复和分布变化
    a = [(i * 2 + 3) % (2 * n + 5) + 1 for i in range(N)]

    a.sort()

    ans = 0
    c = 1

    for i in range(N):
        if c > a[N - 1] or c > a[i]:
            ans += a[i] - 1
            continue
        if i != N - 1:
            ans += a[i] - 1
            c += 1
        else:
            ans += c - 1

    print(ans)
    return ans


if __name__ == "__main__":
    main(10)