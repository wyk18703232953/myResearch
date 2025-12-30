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
    # 根据规模 n 生成测试数据：
    # 原程序有两个参数 a, b，这里设 a = n，b = n // 2 作为示例测试数据。
    a = n
    b = n // 2
    ans = big(a, b)
    print(ans)


if __name__ == "__main__":
    # 示例：可修改 n 来测试不同规模
    main(10**6)