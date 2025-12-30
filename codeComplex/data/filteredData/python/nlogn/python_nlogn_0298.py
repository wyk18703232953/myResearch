import random

def main(n: int):
    # 1. 生成测试数据
    # 生成 n 个权值（1 到 10^9 之间的随机整数）
    w_values = [random.randint(1, 10**9) for _ in range(n)]
    # 生成长度为 2n 的 01 序列，其中包含 n 个 '0' 和 n 个 '1'
    # 保证前缀中 0 的数量始终不少于 1 的数量（即有效的栈操作序列）
    # 简单构造：先生成一个随机合法括号序列，用 0 表示入栈(选最小), 1 表示出栈
    seq = []
    open_cnt = 0
    close_cnt = 0
    for _ in range(2 * n):
        # 若还可以放 0
        choices = []
        if open_cnt < n:
            choices.append('0')
        if close_cnt < open_cnt:
            choices.append('1')
        c = random.choice(choices)
        seq.append(c)
        if c == '0':
            open_cnt += 1
        else:
            close_cnt += 1
    k = ''.join(seq)

    # 2. 原程序逻辑
    w = [(w_values[c], c + 1) for c in range(n)]
    b = sorted(w, reverse=True)
    f = []
    p = []
    for ch in k:
        if ch == "0":
            x = b.pop()
            f.append(x)
            p.append(x[1])
        else:
            y = f.pop()
            p.append(y[1])

    print(*p)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)