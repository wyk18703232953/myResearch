def dig(d):
    return ord(d) - ord('0')


def biggest_left(counts):
    res = ''
    for i in range(9, -1, -1):
        res += str(i) * counts[i]
    return res


def ok(d, _counts, rest):
    if rest == '':
        return True

    counts = _counts.copy()
    counts[d] -= 1

    r = ''
    for i in range(10):
        r += str(i) * counts[i]

    return int(r) <= int(rest)


def main():
    a, b = input(), input()

    counts = [0] * 10
    for d in a:
        counts[dig(d)] += 1

    ans = ''
    if len(a) < len(b):
        print(biggest_left(counts))
        return

    n = len(a)
    for i in range(n):
        d = dig(b[i])

        if counts[d] and ok(d, counts, b[i+1:]):
            ans += b[i]
            counts[d] -= 1
        else:
            for s in range(d-1, -1, -1):
                if counts[s] > 0:
                    ans += str(s)
                    counts[s] -= 1
                    ans += biggest_left(counts)
                    print(ans)
                    return
    print(ans)


if __name__ == '__main__':
    main()
