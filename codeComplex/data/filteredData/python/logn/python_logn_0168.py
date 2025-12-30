def prod(n: int) -> int:
    if n % 2:
        return n * ((n + 1) // 2)
    else:
        return (n // 2) * (n + 1)


def total_count(n: int, k: int):
    if k >= n:
        return 0, 0, 1
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
        return n, k, count


def solve_single(n: int, k: int) -> int:
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
    """
    根据规模 n 生成测试数据并输出结果。
    这里约定测试数据为：
        - n 保持为传入规模
        - k 取一个与 n 同量级的值，这里设为 n // 2 + 1（保证 k >= 1）
    如需其他生成策略，可在此处修改。
    """
    if n <= 0:
        return

    # 测试数据生成策略：k 与 n 同量级
    k = max(1, n // 2 + 1)

    ans = solve_single(n, k)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    main(10)