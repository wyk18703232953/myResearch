import random

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
        n, k, count = total_count(n, k)
        if n:
            return count + 2
        else:
            return count + 1


def main(n: int):
    # 根据规模 n 生成测试数据：
    # 约束：1 <= n <= n_max, 1 <= k <= n
    if n <= 0:
        return  # 不做任何输出

    # 生成一个与规模 n 相关的 n_val 和 k_val
    n_val = n
    k_val = random.randint(1, n_val)

    ans = solve(n_val, k_val)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)