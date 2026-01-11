def main(n):
    # 映射含义：
    # n -> 数组长度 n，k 固定为 n//2 + 1（保证 1 <= k <= n）
    if n < 2:
        # 原算法在 n-1 上有操作，这里保证 n>=2
        n = 2

    k = n // 2 + 1
    if k > n:
        k = n

    # 确定性生成数组 arr，长度为 n
    # 示例构造：arr[i] = i^2 - i
    arr = [i * i - i for i in range(n)]

    kek = [0] * (n - 1)
    for i in range(n - 1):
        kek[i] = -arr[i + 1] + arr[i]

    kek.sort()

    ans = arr[-1] - arr[0]
    for i in range(k - 1):
        ans += kek[i]

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)