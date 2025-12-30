def sm(n):
    return n * (n + 1) // 2

def summ(en, st):
    if st <= 1:
        return sm(en)
    return sm(en) - sm(st - 1)

def bs(n, k):
    st = 1
    en = k
    while st < en:
        md = (st + en) // 2
        s = summ(k, md)
        if s == n:
            return k - md + 1
        elif s > n:
            st = md + 1
        else:
            en = md
    return k - st + 2

def solve_one(n, k):
    if n == 1:
        return 0
    elif n <= k:
        return 1
    else:
        n -= 1
        k -= 1
        if sm(k) < n:
            return -1
        else:
            return bs(n, k)

def main(n):
    """
    使用规模参数 n 生成测试数据 (n,k)，并输出结果。
    这里约定：k = n，用于自动生成一组测试数据。
    若需其他生成策略可按需修改。
    """
    k = n  # 简单的数据生成策略：令 k = n
    ans = solve_one(n, k)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改 n 的值
    main(10)