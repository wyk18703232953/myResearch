def pow10(i):
    n = 1
    for _ in range(i):
        n *= 10
    return n

def solve(k):
    n = 0
    i = 0
    while k > n:
        n += pow10(i) * 9 * (i + 1)
        i += 1
    n -= pow10(i - 1) * 9 * i
    k -= n
    t = (k - 1) // i
    r = k % i
    if r == 0:
        r = i
    m = pow10(i - 1) + t
    ans = (m // pow10(i - r)) % 10
    return ans

def main(n):
    # 根据规模 n 生成测试数据，这里示例：k = n
    k = n
    result = solve(k)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(1000)
    main(1000)