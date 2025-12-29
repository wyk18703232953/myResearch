MOD = 998244353

def main(n):
    # 根据规模 n 生成测试数据，这里示例为 a[i] = i+1
    a = [i + 1 for i in range(n)]

    p, sp, s, ss = 0, 0, 0, 0
    for x in a:
        ss = (2 * ss + s) % MOD
        s = (s + x) % MOD
        p = (ss + sp + s) % MOD
        sp = (sp + p) % MOD
    print(p)


if __name__ == '__main__':
    # 示例：调用 main(5)
    main(5)