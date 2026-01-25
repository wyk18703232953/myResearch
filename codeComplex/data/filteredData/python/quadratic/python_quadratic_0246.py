def main(n):
    # 对于原程序：输入结构为单行三个整数 n, a, b
    # 这里将 n 视为原问题中的 n
    # a, b 由 n 确定性生成：a = 1, b = 1（保证可行且能覆盖 m == 1 分支）
    a = 1
    b = 1

    if min(a, b) > 1:
        print('NO')
        return

    m = max(a, b)

    if m == 1:
        if n == 1:
            print('YES')
            print(0)
            return
        elif n < 4:
            print('NO')
            return
        else:
            print('YES')
            for row in range(n):
                line = ['0'] * n
                if row > 0:
                    line[row - 1] = '1'
                if row < n - 1:
                    line[row + 1] = '1'
                print(''.join(line))
        return

    print('YES')

    if a == 1:
        c = '1'
        d = '0'
    else:
        c = '0'
        d = '1'

    for row in range(n):
        if row < m - 1:
            line = [c] * n
        else:
            line = [c] * (m - 1) + [d] * (n - m + 1)
        line[row] = '0'
        print(''.join(line))


if __name__ == "__main__":
    # 示例调用：以 5 作为规模
    main(5)