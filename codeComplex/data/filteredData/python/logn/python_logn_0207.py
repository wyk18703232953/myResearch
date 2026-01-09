def digit(x: int) -> int:
    res = 0
    while x:
        res += x % 10
        x //= 10
    return res


def solve(n: int, s: int) -> int:
    l, r = s, 10**18 + 7
    while l < r:
        m = (l + r) // 2
        if m - digit(m) < s:
            l = m + 1

        else:
            r = m
    return max(0, n - l + 1)


def main(n: int) -> None:
    # 根据规模 n 生成测试数据：
    # 这里给出一种简单策略：令 s 为 n 的一半（可按需要修改）
    s = n // 2
    ans = solve(n, s)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10**6) 进行测试
    main(10**6)