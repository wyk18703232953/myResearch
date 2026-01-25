def main(n):
    # 映射规则：
    # m = n（元素个数）
    # k = n//3 + 1（页大小，避免为 0）
    # p 为长度为 m 的递增数组，元素为 (i+1)*2
    m = n
    if m <= 0:
        print(0)
        return
    k = n // 3 + 1
    p = [(i + 1) * 2 for i in range(m)]

    count = 0
    delete = 0
    now = 0
    while now < m:
        up = ((p[now] - delete - 1) // k + 1) * k + delete
        while now < m and p[now] <= up:
            now += 1
            delete += 1
        count += 1
    print(count)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)