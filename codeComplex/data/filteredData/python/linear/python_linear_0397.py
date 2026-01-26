mod = 998244353

def main(n):
    ans = 0
    # 生成确定性的长度为 n 的整数序列
    a = [(i * 3 + 7) % mod for i in range(n)]
    p = 1 / 2
    for i in range(n):
        ans = (ans + (i + 2) * (p * a[n - i - 1] % mod) % mod) % mod
        p = (2 * p) % mod
    # print(int(ans) % mod)
    pass
if __name__ == "__main__":
    main(10)