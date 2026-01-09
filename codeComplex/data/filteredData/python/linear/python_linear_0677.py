def f(a):
    b = [a[0]]
    for e in a[1:]:
        if b != []:
            if e == b[-1] or abs(e - b[-1]) % 2 == 0:
                b.pop()

            else:
                b.append(e)

        else:
            b.append(e)

    for i in range(1, len(b)):
        if abs(b[i] - b[i - 1]) % 2:
            # print('NO')
            pass
            return

    # print('YES')
    pass


def main(n):
    if n <= 0:
        return
    # 生成确定性的长度为 n 的数组 a
    # 这里使用简单的算术构造：a[i] = (i % 5) - 2
    a = [(i % 5) - 2 for i in range(n)]
    f(a)


if __name__ == "__main__":
    main(10)