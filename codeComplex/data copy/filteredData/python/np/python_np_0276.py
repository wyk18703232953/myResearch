def solve(n, m, ops):
    h = m & -m
    for c in ops:
        if c == 'U' and m != (n + 1) >> 1:
            m += -h if (m + h) % (h << 2) == 0 else h
            h <<= 1
        if c in 'LR' and h > 1:
            h >>= 1
            m += -h if c == 'L' else h
    return m

def main(n):
    # 解释规模含义：
    # n >= 2
    # 使用原程序输入结构：
    # 第一行: n m
    # 接下来 m 行: 每行一个整数(节点)和一串操作
    # 这里：m = n，节点为 1..n，操作串长度也与 n 相关
    if n < 2:
        n = 2

    total_nodes = n
    m = n  # 作为测试用例数量

    # 为每个测试生成确定性操作序列：
    # 第 i 个测试的操作串长度为 L = (i % n) + 1
    # 位置 j 的操作为:
    #   k = (i + j) % 3
    #   k == 0 -> 'U', k == 1 -> 'L', k == 2 -> 'R'
    results = []
    for i in range(1, m + 1):
        # 节点值在 [1, n] 内循环
        node = (i % total_nodes) + 1

        L = (i % n) + 1
        ops_chars = []
        for j in range(L):
            k = (i + j) % 3
            if k == 0:
                ops_chars.append('U')
            elif k == 1:
                ops_chars.append('L')
            else:
                ops_chars.append('R')
        ops = ''.join(ops_chars)

        res = solve(total_nodes, node, ops)
        results.append(res)

    for x in results:
        print(x)

if __name__ == "__main__":
    main(10)