def digit(a: int) -> int:
    s = 0
    while a:
        s += a % 10
        a //= 10
    return s


def big(n: int, s: int) -> int:
    lo = 1
    hi = n
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid - digit(mid) < s:
            lo = mid + 1
        else:
            hi = mid - 1
    return n - lo + 1


def main(n: int):
    """
    n: 问题规模（用作原代码中的 a）
    这里根据 n 生成测试数据：
    - 令 s 与 n 同阶，这里简单设为 s = n // 2
    """
    a = n
    b = n // 2  # 测试数据生成策略，可按需要修改
    ans = big(a, b)
    print(ans)


if __name__ == "__main__":
    # 示例：以 n = 100 为规模运行
    main(100)