def binary_search(n, k):
    left = -1
    right = n
    while left < right - 1:
        middle = (left + right) // 2
        if middle % 2 != 0:
            s = (1 + middle) * (middle // 2) + ((1 + middle) // 2)

        else:
            s = (1 + middle) * (middle // 2)
        if s - (n - middle) >= k:
            right = middle

        else:
            left = middle
    return right


def main(n):
    # 根据 n 生成测试数据，这里简单设置 k 为 n 的一半
    k = max(1, n // 2)
    # print(n - binary_search(n, k))
    pass
if __name__ == "__main__":
    # 示例：可以在此修改 n 以测试不同规模
    main(10)