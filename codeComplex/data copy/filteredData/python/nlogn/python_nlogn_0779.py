def main(n):
    # 映射：n 为数组长度，k 设为 n//3+1，保证 1 <= k <= n
    if n <= 1:
        # print(0)
        pass
        return

    k = n // 3 + 1
    if k > n:
        k = n

    # 确定性生成数组：严格递增
    arr = [i * 2 + (i % 3) for i in range(n)]

    diff = [0] * (n - 1)
    p = arr[-1] - arr[0]
    for i in range(n - 1):
        diff[i] = arr[i + 1] - arr[i]
    diff.sort(reverse=True)
    if k - 1 > 0:
        result = p - sum(diff[:k - 1])

    else:
        result = p
    # print(result)
    pass
if __name__ == "__main__":
    main(10)