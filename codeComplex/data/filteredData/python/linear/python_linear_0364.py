def main(n):
    # n 表示每个列表的长度规模
    m = n

    # 确定性生成 a 和 b
    # a: 递增序列，从 1 到 n
    a = [i + 1 for i in range(n)]

    # b: 递增序列，从 0 到 m-1，每个元素加上偏移量 2
    b = [i + 2 for i in range(m)]

    ans = 0
    for i in range(len(a)):
        if len(b) == 0:
            break
        if b[0] >= a[i]:
            ans += 1
            del b[0]
    print(ans)


if __name__ == "__main__":
    main(10)