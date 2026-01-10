def main(n):
    # n 表示数组长度 m，数值 n 与 m 相同规模
    m = n
    # 确定性地生成数组 a：例如 a[i] = (i * 2) % (n // 2 + 1) 保证有重复和变化
    if n <= 0:
        a = []
    else:
        base = n // 2 + 1
        a = [(i * 2) % base for i in range(m)]

    ans = sum(a)
    a.sort()
    lastlevel = 0
    level = 0
    got = 0

    for i in a:
        got = max(got, i)
        level = min(level + 1, got)
        if i > 0:
            ans -= 1
            lastlevel = level

    ans -= (got - level)
    print(ans)


if __name__ == "__main__":
    # 示例：使用 n=10 作为输入规模
    main(10)