def main(n):
    # 根据 n 生成测试数据
    # 这里构造：
    # m = n，k 取一个中等大小的值（例如 n//3+1），
    # p 为 1..m 的顺序数组（可根据需要调整生成方式）
    m = n
    k = max(1, n // 3 + 1)
    p = list(range(1, m + 1))

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