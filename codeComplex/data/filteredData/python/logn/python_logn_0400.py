from sys import stdout

def main(n):
    """
    根据给定规模 n 生成对应的序列，并输出到 stdout。
    原逻辑来自去除 input() 的版本。
    """
    w = n
    d = 1
    p = []
    cur_n = n

    # 按原程序逻辑构造序列
    while cur_n != 1:
        t = (cur_n + 1) // 2
        for _ in range(t):
            p.append(str(d))
        cur_n -= t
        if cur_n == 1:
            break
        d *= 2

    # 处理最后一个数
    if w % d == 0:
        p.append(str(w))
    else:
        g = w // d
        r = d * g
        p.append(str(r))

    stdout.write(" ".join(p))

if __name__ == "__main__":
    # 示例：使用 n = 10 作为测试规模
    main(10)