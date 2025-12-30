from sys import stdout

MOD = 1000000007


def main(n):
    # 1. 生成规模为 n 的测试数据
    # 这里简单生成一个长度为 n 的01串，以及 q 组区间查询
    # 你可以根据需要修改数据生成方式
    a = ''.join('01'[(i * 37) % 2] for i in range(n))  # 交替01串的一种构造方式
    q = n  # 简单设定 q = n
    queries = []
    for i in range(q):
        # 生成合法区间 1-based: (l, r)，这里构造 l = 1..n, r = n
        l = i + 1
        r = n
        queries.append((l, r))

    # 2. 原逻辑开始
    o = []  # 前缀 0 的数量
    s = []  # 前缀 1 的数量
    cnt0 = cnt1 = 0

    for ch in a:
        if ch == '0':
            cnt0 += 1
        else:
            cnt1 += 1
        o.append(cnt0)
        s.append(cnt1)

    # 预计算 2 的幂
    z = [1]
    for _ in range(100000):
        z.append((z[-1] * 2) % MOD)

    out_lines = []
    for l, r in queries:
        length = r - l + 1
        # 区间内 0 的数量
        zs = o[r - 1] - (o[l - 2] if l > 1 else 0)
        # 区间内 1 的数量
        os = length - zs

        if zs != 0:
            val = ( (z[os] - 1) % MOD * z[zs] ) % MOD
        else:
            val = (z[os] - 1) % MOD
        out_lines.append(str(val))

    stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可根据需要修改 n
    main(10)