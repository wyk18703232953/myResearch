def main(n):
    # 生成长度为 n 的确定性数组
    a = [(i * 2 + 3) % (n + 5) + 1 for i in range(n)]
    a = sorted(a, reverse=True)
    s1 = 0
    s2 = sum(a)

    for i in range(len(a)):
        s1 += a[i]
        s2 -= a[i]
        if s1 > s2:
            break

    # print(i + 1)
    pass
if __name__ == "__main__":
    main(10)