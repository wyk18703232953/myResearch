def main(n):
    # 映射：n 为两数组的长度，n, m 都取为 n
    # k 与 p 的元素通过简单算术确定性构造
    m = n
    k = [i % 7 for i in range(1, n + 1)]
    p = [((i * 3) % 11) for i in range(1, m + 1)]

    a = 0
    b = 0
    ans = 0
    while a != n and b != m:
        if p[b] >= k[a]:
            ans += 1
            a += 1
            b += 1

        else:
            a += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)