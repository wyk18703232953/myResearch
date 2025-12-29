def main(n):
    # 生成测试数据：根据规模 n 生成 moves, left
    # 这里示例生成：moves = n 的平方，left = n
    # 可根据实际需求更改生成方式
    moves = n * n
    left = n

    l = 1
    r = 10**9 + 1
    while l <= r:
        mid = (l + r) >> 1
        fx = (mid * (mid + 1)) // 2 - left + mid
        if fx <= moves:
            l = mid + 1
        else:
            r = mid - 1
    result = moves - r
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)