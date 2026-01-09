def main(n):
    # 映射含义：
    # n: 数组长度
    # m: 步长，设为 max(1, n // 5)
    # k: 常数扣减，设为 n // 3 + 1 保证随规模增长
    if n <= 0:
        # print(0)
        pass
        return

    m = max(1, n // 5)
    k = n // 3 + 1

    # 生成确定性数组 aa
    # aa[i] = (i % 7) - (i % 3) + 5，既有正有负并随 n 变化
    aa = [(i % 7) - (i % 3) + 5 for i in range(n)]

    ans = 0
    for start in range(m):
        ac = aa[:]
        for i in range(start, n, m):
            ac[i] -= k
        cur = 0
        for i in range(start, n):
            if i % m == start:
                cur = max(ac[i] + cur, ac[i])

            else:
                cur += ac[i]
            ans = max(cur, ans)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(1000)