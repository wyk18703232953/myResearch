def prod(n: int) -> int:
    if n % 2:
        return n * ((n + 1) // 2)

    else:
        return (n // 2) * (n + 1)


def total_count(n: int, k: int):
    if k >= n:
        return (0, 0, 1)

    else:
        count = 0
        l = 1
        r = k
        s = prod(k)
        while l <= r:
            mid = (l + r) // 2
            if n > s - prod(mid) + mid:
                r = mid - 1

            else:
                l = mid + 1

        n = n - (s - prod(l) + l)
        count += (k - l + 1)
        k = l - 1
        return (n, k, count)


def solve(n: int, k: int) -> int:
    if prod(k) - (k - 1) < n:
        return -1
    elif n == 1:
        return 0
    elif k >= n:
        return 1

    else:
        n = n - k
        k = k - 2
        count = 1
        while n > 0:
            n, k, temp = total_count(n, k)
            count += temp
        return count


def main(n: int):
    """
    n: 规模参数，用于生成测试数据 (n_val, k_val)
    这里简单设定：
        n_val = n
        k_val = max(1, n // 2)
    可以根据需要修改生成规则。
    """
    n_val = n
    k_val = max(1, n // 2)
    ans = solve(n_val, k_val)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模测试
    main(10)