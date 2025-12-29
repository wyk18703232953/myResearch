import random

def main(n):
    # 生成测试数据：
    # n: 数组 s 的长度
    # m: 数组 s1 的长度，设为 n 或 n+1（保持同量级）
    m = n if n > 1 else 1

    # 生成 s（战力/价格等整数），范围自定
    s = [random.randint(1, 10**5) for _ in range(n)]
    # 生成 s1，使其大部分 >= max(s)，以避免大量 -1 情况
    base = max(s)
    s1 = [random.randint(base, base + 10**5) for _ in range(m)]

    # 原逻辑开始
    if min(s1) < max(s):
        print(-1)
        return

    s.sort()
    s1.sort()

    ans = 0
    if s1[0] != s[-1]:
        ans += s1[0]
        ans += s[-2] * (m - 1)
        ans += sum(s1[1::])
        ans += s[-1]
        for i in range(n - 2):
            ans += s[i] * m
    else:
        ans += sum(s1)
        for i in range(n - 1):
            ans += s[i] * m
    print(ans)


if __name__ == "__main__":
    # 示例：规模 n=5
    main(5)