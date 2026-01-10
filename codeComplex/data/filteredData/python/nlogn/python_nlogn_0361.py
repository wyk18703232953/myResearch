def main(n):
    # n 表示数组长度
    if n <= 0:
        return

    # 确定性生成长度为 n 的数组 x
    # 构造有规律的整数序列，保证可重复
    # 这里采用稍有变化的序列，避免完全等差导致行为过于单一
    x = [(i * 3 + (i // 2)) % (3 * n + 7) for i in range(n)]
    x.sort()
    s = set(x)

    m, ans = 1, [x[0]]
    pow2 = [1]
    for _ in range(35):
        pow2.append(2 * pow2[-1])

    for i in x:
        for j in pow2:
            if (i - j) in s and (i + j) in s:
                m = 3
                ans = [i - j, i, i + j]
                break
            elif (i - j) in s and m < 2:
                m = 2
                ans = [i, i - j]
            elif (i + j) in s and m < 2:
                m = 2
                ans = [i, i + j]
        if m == 3:
            break

    print(m)
    print(*ans)


if __name__ == "__main__":
    main(10)