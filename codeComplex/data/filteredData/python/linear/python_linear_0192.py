def main(n):
    # 参数生成策略（确定性）：
    # A, B, C, T 与 n 线性相关，保持可扩展
    # 保证 T > max(a[i]) 以及 T > 0
    if n <= 0:
        print(0)
        return

    A = n + 1
    B = (n % 5) + 1
    C = (n % 7) + 1
    T = 2 * n + 5

    # a[i] 为递增但有重复、取模于 T，保证 0 <= a[i] < T
    a = [(i * 3) % T for i in range(n)]

    ans = 0
    for i in range(n):
        su = A
        cur = A
        start = a[i]
        # 在原逻辑中，若 start >= T，循环不会执行；这里 start < T 恒成立
        for j in range(start, T):
            cur -= B
            su = max(su, (j - start + 1) * C + cur)
        ans += su

    print(ans)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)