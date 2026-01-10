def main(n):
    # 规模含义：
    # n: 数组长度
    if n <= 1:
        print(0)
        return

    # 确定性生成 k 和数组 arr
    # 这里让 k 与 n 成线性关系，但保证 1 <= k <= n
    k = n // 3 + 1
    if k > n:
        k = n

    # 生成一个严格递增的数组，便于保持间隔有意义
    # arr[i] = i * 2
    arr = [i * 2 for i in range(n)]

    # 原始逻辑
    k -= 1
    arr_new = sorted([arr[i + 1] - arr[i] for i in range(n - 1)], reverse=True)
    result = arr[-1] - arr[0] - sum(arr_new[:k])
    print(result)


if __name__ == "__main__":
    main(10)