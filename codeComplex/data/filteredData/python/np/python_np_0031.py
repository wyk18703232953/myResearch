def main(n):
    # n 表示数组 a 的长度，元素值范围固定在 [0, 2^20-1]
    mod = 10**9 + 7

    # 确定性构造输入数组 a：使用简单算术构造
    # 例如：a[i] = (i * 1315423911) & ((1 << 20) - 1)
    limit = 1 << 20
    a = [((i * 1315423911) & (limit - 1)) for i in range(n)]

    b = [0] * limit
    for i in range(n):
        b[a[i]] += 1

    for i in range(20):
        step = 1 << i
        for j in range(limit):
            if (j & step) == 0:
                b[j] += b[j | step]

    ans = 0
    for i in range(limit):
        cnt = bin(i).count("1")
        val = pow(2, b[i], mod) - 1
        if cnt % 2 == 0:
            ans += val
        else:
            ans -= val
        ans %= mod

    print(ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(100000)