def main(n: int):
    # 生成测试数据：n 给定，k 在合法范围内取一个值
    # 原式：mid*(mid+1)/2 - (n-mid) 取值范围大致为 [-(n), n(n+1)/2]
    # 简单起见，我们取 k 为表达式在 mid = n//2 处的值
    mid0 = n // 2
    k = mid0 * (mid0 + 1) // 2 - (n - mid0)

    l = 0
    r = n
    while l <= r:
        mid = (l + r) // 2
        val = mid * (mid + 1) // 2 - (n - mid)
        if val < k:
            l = mid + 1
        elif val > k:
            r = mid
        else:
            # 原代码输出的是 n - mid
            print(n - mid)
            return mid

    # 若二分未找到（理论上不应发生），可返回 None
    return None


if __name__ == '__main__':
    # 示例：调用 main，规模 n 可调整
    main(10)