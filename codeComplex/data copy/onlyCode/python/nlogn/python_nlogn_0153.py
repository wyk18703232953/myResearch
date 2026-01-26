def func(k, a):
    if len(a) == 1:
        return 1
    if k == 1:
        return len(a)
    s = set(a)
    for x in sorted(a):
        if x in s and k * x in s:
            s.remove(k * x)
    return len(s)


def read_ints():
    return [int(x) for x in input().split(' ')]


def main():
    n, k = read_ints()
    a = read_ints()
    assert n == len(a)
    print(func(k, a))


if __name__ == '__main__':
    main()
