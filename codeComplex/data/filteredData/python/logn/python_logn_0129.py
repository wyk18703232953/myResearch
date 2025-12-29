def s(n):
    return (n * (n + 1)) // 2

def diff(st, en):
    return s(en) - s(st - 1)

def bs(k, n):
    st = 1
    en = k
    while st < en:
        mid = (st + en) // 2
        total = diff(mid, k)
        if total == n:
            return k - mid + 1
        if total > n:
            st = mid + 1
        else:
            en = mid
    return k - st + 2

def solve_single(n, k):
    if n == 1:
        return 0
    if n <= k:
        return 1
    n -= 1
    k -= 1
    if s(k) < n:
        return -1
    return bs(k, n)

def main(n):
    """
    按规模 n 生成一组测试数据 (N, K)，并返回原程序的输出结果。
    这里简单生成：
      N = n
      K = max(1, min(n, n // 2 + 1))
    """
    if n <= 0:
        return None  # 无意义规模

    N = n
    K = max(1, min(n, n // 2 + 1))
    return solve_single(N, K)

if __name__ == '__main__':
    # 示例：运行若干规模的测试
    for size in [1, 2, 5, 10, 20]:
        print(size, main(size))