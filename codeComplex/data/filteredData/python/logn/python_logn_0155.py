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

def solve(n, k):
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
    n 为规模参数，这里用于生成测试数据:
    设定 k = n，用原逻辑计算结果。
    """
    k = n
    result = solve(n, k)
    print(result)

if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)