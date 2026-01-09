import sys


def main(n):
    # 对于原程序：第一行是 "n k"，第二行是长度为 n 的数组 p
    # 这里将 n 直接作为数组长度使用，并构造确定性的 k 和 p
    if n <= 0:
        return

    k = max(1, n // 2)  # 规模随 n 增长的确定性参数
    p = [(i * 2 + 1) % (2 * n + 3) for i in range(n)]  # 长度为 n 的整数列表

    t = []
    g = {}
    for x in p:
        if x in g:
            t.append(g[x])
            continue
        kk = x - 1
        while True:
            if kk in g:
                if x - g[kk] < k:
                    ttt = g[kk]

                else:
                    ttt = kk + 1
                for i in range(kk + 1, x + 1):
                    g[i] = ttt
                t.append(g[x])
                break
            elif kk < 0 or x - kk == k:
                for i in range(kk + 1, x + 1):
                    g[i] = kk + 1
                t.append(g[x])
                break
            kk -= 1

    sys.stdout.write(' '.join(str(x) for x in t) + '\n')


if __name__ == "__main__":
    # 示例调用：使用一个固定的 n 以便直接运行
    main(10)