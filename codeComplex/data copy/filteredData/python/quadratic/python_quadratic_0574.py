import sys

def countR(ip):
    c = 0
    for i in ip:
        if i == 'R':
            c += 1
    return c

def countB(ip):
    c = 0
    for i in ip:
        if i == 'B':
            c += 1
    return c

def countG(ip):
    c = 0
    for i in ip:
        if i == 'G':
            c += 1
    return c

def solve_one(n, k, a):
    x = 'RGB' * 680
    y = 'GBR' * 680
    z = 'BRG' * 680
    xk = x[:k]
    yk = y[:k]
    zk = z[:k]
    op = 2001
    for j in range(n - k + 1):
        b = a[j:j + k]
        xd = 0
        yd = 0
        zd = 0
        for jj in range(len(b)):
            if b[jj] != xk[jj]:
                xd += 1
            if b[jj] != yk[jj]:
                yd += 1
            if b[jj] != zk[jj]:
                zd += 1
        op = min(op, xd, yd, zd)
    return op

def main(n):
    # 确定性构造多组测试数据：
    # t: 测试用例数量
    # n: 作为字符串长度的上界尺度
    # 每组：n_i = i + 1, k_i = max(1, (i % n_i) + 1), a_i 由 'RGB' 周期性构成并在部分位置替换
    if n <= 0:
        return

    t = n
    results = []
    for i in range(1, t + 1):
        length = i
        k = (i % length) + 1
        pattern = "RGB"
        base = (pattern * ((length // 3) + 1))[:length]
        chars = list(base)
        for j in range(0, length, 2):
            c = chars[j]
            if c == 'R':
                chars[j] = 'G'
            elif c == 'G':
                chars[j] = 'B'

            else:
                chars[j] = 'R'
        a = "".join(chars)
        res = solve_one(length, k, a)
        results.append(res)

    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(5)