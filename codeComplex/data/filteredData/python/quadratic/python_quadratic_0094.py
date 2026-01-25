def main(n):
    # n 表示矩阵规模 N
    N = max(1, int(n))

    # 确定性构造 m1 和 m2，每行是长度为 N 的字符串
    # 使用简单的算术模式，保证同一 n 下结果恒定
    m1 = []
    m2 = []
    for i in range(N):
        row1 = ''.join(chr(ord('a') + (i + j) % 26) for j in range(N))
        row2 = ''.join(chr(ord('z') - (i * 2 + j) % 26) for j in range(N))
        m1.append(row1)
        m2.append(row2)

    ms = [
        m2,
        [x[::-1] for x in m2],
        [x for x in reversed(m2)],
    ]

    a = []
    for m in ms:
        a.append(m)
        a.append([x[::-1] for x in reversed(m)])
        a.append([''.join(m[j][i] for j in range(N - 1, -1, -1)) for i in range(N)])
        a.append([''.join(m[j][i] for j in range(N)) for i in range(N - 1, -1, -1)])

    ms = a
    result = ['NO', 'YES'][m1 in ms]
    print(result)
    return result


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的取值
    main(5)