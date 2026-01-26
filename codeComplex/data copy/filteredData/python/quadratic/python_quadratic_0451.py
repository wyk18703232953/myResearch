def main(n):
    # n 表示序列长度
    if n <= 0:
        return

    # 确定性构造 L：1..n 的简单排列
    # 使用一个线性同余式打散顺序，保证对每个 n 唯一且确定
    L = [((i * 37 + 23) % n) + 1 for i in range(n)]

    ans = [''] * n
    revL = [0] * n
    ans[-1] = 'B'

    for i in range(n):
        revL[L[i] - 1] = i + 1

    for i in range(n - 2, -1, -1):
        t = revL[i] - 1
        counter = 'B'
        for j in range(t, -1, -i - 1):
            if j == t:
                continue
            if ans[L[j] - 1] == 'B':
                counter = 'A'
                break
        if counter != 'A':
            for k in range(t, n, i + 1):
                if k == t:
                    continue
                if ans[L[k] - 1] == 'B':
                    counter = 'A'
                    break
        ans[i] = counter

    # 保持原先输出结构：按 L 的顺序输出对应的字符，不含分隔符和换行
    output = ''.join(ans[L[i] - 1] for i in range(n))
    # print(output, end='')
    pass
if __name__ == "__main__":
    # 示例：使用固定规模 n 运行
    main(10)