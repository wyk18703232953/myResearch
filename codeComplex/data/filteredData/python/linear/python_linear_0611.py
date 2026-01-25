def main(n):
    # n: 输入规模，对应原程序中的 n
    # ai, bi 都是长度为 n 的整数序列，取值范围 [1, n]
    if n <= 0:
        return

    # 确定性构造 ai、bi
    # ai: 1, 2, 3, ..., n
    ai = [i + 1 for i in range(n)]
    # bi: 依次向右平移一位的循环序列
    # 例如 n=5 时为 [2,3,4,5,1]
    bi = [(i + 1) % n + 1 for i in range(n)]

    ai2 = [0] * (n + 1)
    n2 = 0
    out = []
    for i in range(n):
        num = 0
        if ai2[bi[i]] != 1:
            for j in range(n2, n):
                ai2[ai[j]] = 1
                if ai[j] == bi[i]:
                    num = j + 1 - n2
                    n2 = j + 1
                    break
        out.append(str(num))
    print(" ".join(out))


if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次时间复杂度实验
    main(10)