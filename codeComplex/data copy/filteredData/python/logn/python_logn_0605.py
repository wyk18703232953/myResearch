def binary(n, k, low, high):
    if low <= high:
        mid = (low + high) // 2
        val = (mid * (mid + 1)) // 2 - (n - mid)
        if val == k:
            return n - mid
        elif val > k:
            return binary(n, k, low, mid - 1)

        else:
            return binary(n, k, mid + 1, high)
    return None  # 未找到时的兜底返回，可按需要调整


def main(n):
    # 根据 n 生成测试数据：
    # 这里构造一个合法的 k：选择某个 mid，在范围 [1, n] 内
    mid = n // 2 if n >= 2 else 1
    k = (mid * (mid + 1)) // 2 - (n - mid)

    result = binary(n, k, 1, n)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main，使用某个规模 n
    main(10)