def main(n):
    # 映射：n -> 数组长度 n，k 为 n//3 + 1（保证 1 <= k <= n）
    if n <= 0:
        return
    k = n // 3 + 1
    if k > n:
        k = n

    # 构造确定性递增数组 data，差分有变化，便于模拟一般情况
    # data[i] = i * (i % 5 + 1)
    data = [i * (i % 5 + 1) for i in range(n)]

    span = data[-1] - data[0]
    delta = [data[i + 1] - data[i] for i in range(n - 1)]
    delta.sort(reverse=True)
    result = span - sum(delta[:k - 1]) if k > 0 else span
    # print(result)
    pass
if __name__ == "__main__":
    main(10)