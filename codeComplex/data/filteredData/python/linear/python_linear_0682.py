def main(n):
    # n 表示原程序中整数序列 a 的长度（原程序第一行输入是 2*n）
    n = int(n)
    m = 2 * n  # 对应原始的第一个输入

    # 构造确定性输入序列 a，长度为 m
    # 这里使用简单的算术生成：a[i] = (i * 3) % (m + 5)
    a = [(i * 3) % (m + 5) for i in range(m)]

    # 以下保持原程序核心逻辑不变，仅将 input() 替换为构造的 a
    n_half = m // 2
    b = [0] * n_half
    a_rev = list(reversed(a))
    for x in a_rev:
        b.append(x)

    mem = b[-1]
    c = 0
    for i in range(n_half - 1):
        if b[-2 - i] - c > mem:
            c = b[-2 - i] - mem
        b[-2 - i] -= c
        b[1 + i] += c
        mem = b[-2 - i]

    # 为保持实验可控，这里返回 b，而不是直接打印
    return b


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的规模
    result = main(5)
    # print(" ".join(map(str, result)))
    pass