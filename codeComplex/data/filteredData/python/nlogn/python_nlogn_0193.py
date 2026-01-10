def main(n):
    a = {}
    ans = 0
    s = 0
    i = 0
    # 生成长度为 n 的确定性整数序列，元素值大小与 n 同阶
    # 例如：a_i = i % 10 + i // 10
    arr = [i % 10 + i // 10 for i in range(n)]
    for t in arr:
        s += t
        a[t] = a.get(t, 0) + 1
        ans += (i - a.get(t, 0) - a.get(t - 1, 0) - a.get(t + 1, 0) + 1) * t - (
            s
            - a.get(t, 0) * t
            - a.get(t - 1, 0) * (t - 1)
            - a.get(t + 1, 0) * (t + 1)
        )
        i += 1
    print(ans)


if __name__ == "__main__":
    main(10)