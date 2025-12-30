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
    # 令 a = n（上界规模）
    # 令 b = n // 2（阈值，保证随 n 变化）
    a = n
    b = n // 2
    ans = big(a, b)
    print(ans)

if __name__ == "__main__":
    # 示例：以 n = 10 为规模运行
    main(10)