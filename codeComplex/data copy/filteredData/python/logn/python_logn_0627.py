def binarySearch(N, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        Temp = (mid * (mid + 1)) // 2
        if Temp - x == N - mid:
            return N - mid
        elif Temp - x > N - mid:
            return binarySearch(N, l, mid - 1, x)

        else:
            return binarySearch(N, mid + 1, r, x)

    else:
        return -1


def main(n):
    # 根据规模 n 生成测试数据：
    # 这里简单设 k = n // 2 作为示例测试值
    k = n // 2
    result = binarySearch(n, 0, n, k)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例运行：可根据需要修改 n 的值
    main(10)