def main(n):
    if n <= 0:
        print("")
        return

    # 构造一个确定性的长度为 n 的数组 a
    # 这里用一个简单的算术序列，使数据依赖于 n 且可重复
    a = [(i * 2 + 3) % (n + 5) + 1 for i in range(n)]

    s = [0] * n
    m = n
    while m:
        for i, x in enumerate(a):
            if s[i] == 0:
                if x == 0:
                    continue
                r = range(i % x, n, x)
                if all(a[j] <= x or s[j] == 'A' for j in r):
                    s[i] = 'B'
                    m -= 1
                    if m == 0:
                        break
                if any(a[j] > x and s[j] == 'B' for j in r):
                    s[i] = 'A'
                    m -= 1
                    if m == 0:
                        break
    print(''.join(s))


if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)