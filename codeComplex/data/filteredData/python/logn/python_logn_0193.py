import random

mod = 10**9 + 7

def main(n):
    # 根据规模 n 生成测试数据
    # 题意：给定 n, s，求满足 x - sum_digits(x) >= s 的 x 在 [1, n] 中的个数
    # 这里按照 n 的规模生成 s，使得 0 <= s <= n
    s = random.randint(0, n)

    l = s
    h = n
    ans = n + 1

    while l <= h:
        m = (l + h) // 2

        t = 0
        for ch in str(m):
            t += int(ch)

        if m - t >= s:
            ans = m
            h = m - 1
        else:
            l = m + 1

    print(n - ans + 1)


if __name__ == "__main__":
    # 可以在此处指定规模 n 做测试
    main(10**6)