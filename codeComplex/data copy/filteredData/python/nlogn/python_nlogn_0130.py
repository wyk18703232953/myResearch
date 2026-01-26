def main(n):
    # 映射：n -> 数组长度
    # 构造确定性的 m, k, arr
    m = n * (n + 1) // 4 + 1  # 约为总和的一半多一点
    k = n // 2 + 1
    arr = [(i % (k + 5)) + 1 for i in range(1, n + 1)]
    arr.sort()
    arr = arr + [k]
    ans = 0
    s = 0
    while ans < n + 1:
        s += arr[-ans - 1]
        if s >= m:
            break
        ans += 1
        s -= 1
    if s >= m:
        # print(ans)
        pass

    else:
        # print("-1")
        pass
if __name__ == "__main__":
    main(10)