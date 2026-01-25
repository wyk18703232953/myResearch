def main(n):
    # n 表示字符串数量；每个字符串长度 m 也由 n 确定
    if n <= 0:
        return

    m = max(1, n // 2)

    # 确定性生成 n 个长度为 m 的只含 '0' 和 '1' 的字符串
    A = []
    for i in range(n):
        row_bits = []
        x = i
        for j in range(m):
            # 简单确定性构造：按位取 (i+j) 的奇偶性
            bit = ((i + j) % 2)
            row_bits.append(str(bit))
        A.append(''.join(row_bits))

    C = [0] * m
    for i in range(n):
        a = A[i]
        for j, c in enumerate(a):
            C[j] += int(c)

    for i in range(n):
        a = A[i]
        for j, c in enumerate(a):
            C[j] -= int(c)
        for j in range(m):
            if C[j] == 0:
                break
        else:
            print('YES')
            return
        for j, c in enumerate(a):
            C[j] += int(c)
    print('NO')


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值
    main(10)