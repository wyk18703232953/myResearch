import random

MOD = 10 ** 9 + 7

def main(n):
    # 1. 生成规模为 n 的测试数据
    # 生成一个长度为 n 的随机 01 串
    s = 'x' + ''.join(random.choice('01') for _ in range(n))

    # 设置查询数量 q，并随机生成 q 个区间查询
    # 这里选择 q 与 n 同阶，可按需调整
    q = n
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 2. 原逻辑处理部分
    c = [0] * (n + 1)
    for i in range(1, n + 1):
        c[i] = c[i - 1] + (s[i] == '1')

    p2 = [1] * (2 * n + 1)
    for i in range(1, 2 * n + 1):
        p2[i] = p2[i - 1] * 2 % MOD

    out = []
    for l, r in queries:
        o = c[r] - c[l - 1]
        z = (r - l + 1) - o
        ans = (p2[o + z] - 1 - p2[z] + 1) % MOD
        out.append(ans)

    # 输出结果
    print(*out, sep='\n')


if __name__ == "__main__":
    # 示例运行：可以根据需要修改 n
    main(10)