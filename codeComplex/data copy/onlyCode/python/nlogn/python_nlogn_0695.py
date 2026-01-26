import sys

IS_LOCAL = False


def readMultiple(f):
    return f(map(int, input().split()))


def main():
    n = 3
    a = [1, 2, -4]

    if not IS_LOCAL:
        n = int(input())
        a = readMultiple(list)

    for i, x in enumerate(a):
        if x >= 0:
            a[i] = -x - 1

    cnt_neg = 0
    for x in a:
        if x < 0:
            cnt_neg += 1

    b = sorted([(abs(x), i) for i, x in enumerate(a)])
    if cnt_neg % 2 == 1:
        ind = b[n-1][1]
        a[ind] = -a[ind] - 1

    print(' '.join(map(str, a)))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'True':
        IS_LOCAL = True
    main()
