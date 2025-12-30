def pow4(x, p):
    ret = 1
    for _ in range(p):
        ret = ret * x
    return ret

def rate(p):
    ret = 0
    now = 1
    for _ in range(p):
        ret = ret + now
        now = now * 4
    return ret

def solve(n, k):
    if n > 35:
        return "YES %d" % (n - 1)
    mSplit = 1
    cnt1 = 0
    cnt3 = 1
    for i in range(1, n + 1):
        now = pow4(4, i) - pow4(2, i + 1) + 1
        now = now * rate(n - i) + rate(i)
        if k <= now:
            return "YES %d" % (n - i)
        mSplit = mSplit + cnt1 + cnt3 * 3
        cnt1 = cnt1 + cnt3
        cnt3 = cnt3 + cnt3
        if mSplit > k:
            break
    return "NO"

def main(n):
    """
    规模参数 n：用于生成测试数据。
    生成 n 组 (n_i, k_i) 测试，每组调用一次 solve 并打印结果。
    这里简单生成：
        n_i = i + 1
        k_i = i^2 + 1
    """
    for i in range(n):
        ni = i + 1
        ki = i * i + 1
        res = solve(ni, ki)
        print(res)

if __name__ == "__main__":
    # 示例：规模取 5
    main(5)