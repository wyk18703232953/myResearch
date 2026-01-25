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
            print('NO')
            return

    print('YES')


def main(n):
    if n <= 0:
        return
    a = [i % 10 for i in range(1, n + 1)]
    f(a)


if __name__ == "__main__":
    main(10)