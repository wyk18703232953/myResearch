def func(mid, s):
    p = 0
    q = mid
    while mid > 0:
        p += mid % 10
        mid //= 10
    return (q - p) >= s


def solve(n, s):
    low = 1
    high = 10 ** 18
    ans = n + 1
    while high >= low:
        mid = (high + low) // 2
        if func(mid, s):
            high = mid - 1
            ans = mid
        else:
            low = mid + 1
    if ans > n:
        return 0
    else:
        return n - ans + 1


def main(n):
    """
    规模 n：我们生成一个测试用的 s，并返回结果。
    这里示例：令 s = n // 2（可按需要调整测试数据规则）
    """
    s = n // 2  # 根据 n 生成测试数据
    result = solve(n, s)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main，规模可按需修改
    main(10**6)