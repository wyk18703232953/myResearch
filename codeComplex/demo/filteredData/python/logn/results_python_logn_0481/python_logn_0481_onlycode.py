import sys


def input():
    return sys.stdin.readline().rstrip()


def slv():
    k = int(input())

    def cnt_special(N):
        if N == 0:
            return 0
        return cnt_special(N - 1) + N * (pow(10, N) - pow(10, N - 1))

    def cnt_digit(N):
        ord = len(str(N))
        bound = ord - 1
        return cnt_special(bound) + ord * (N + 1 - 10 ** bound)

    if k < 10:
        print(k)
    else:
        l = 1
        r = int(1e12)
        while r - l > 1:
            med = (r + l)//2
            if cnt_digit(med) >= k:
                r = med
            else:
                l = med
        # cnt_digit(l) < k <= cnt_digit(r)
        rep = k - cnt_digit(l)
        print(str(r)[rep - 1])
        return


def main():
    t = 1
    for i in range(t):
        slv()
    return


if __name__ == "__main__":
    main()
