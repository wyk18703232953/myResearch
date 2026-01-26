def main(n):
    # 约定输入规模：
    # n >= 2 时：
    #   m = n // 2 (步长)
    #   k = max(1, n // 10)
    #   aa 长度 = n，元素为 i % (2*k) - k (保证有正有负)
    # n < 2 时，退化为固定最小规模
    if n < 2:
        n_use = 5

    else:
        n_use = n

    m = max(1, n_use // 2)
    k = max(1, n_use // 10)

    aa = [(i % (2 * k)) - k for i in range(n_use)]

    n_val = n_use
    ans = 0
    for start in range(m):
        ac = aa[:]  # 拷贝数组
        for i in range(start, n_val, m):
            ac[i] -= k
        cur = 0
        for i in range(start, n_val):
            if i % m == start:
                cur = max(ac[i] + cur, ac[i])

            else:
                cur += ac[i]
            ans = max(cur, ans)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用：可自行修改 n 观察规模变化
    main(10)