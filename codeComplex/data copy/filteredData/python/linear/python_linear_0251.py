def solution(n, k):
    ret = [['.' for _ in range(n)] for _ in range(4)]
    if 1 == k & 1:
        ret[1][n >> 1] = '#'
        for i in range(1, n >> 1):
            if k < 2:
                break
            k -= 2
            ret[1][i] = '#'
            ret[1][n - 1 - i] = '#'
        for i in range(1, n >> 1):
            if k < 2:
                break
            k -= 2
            ret[2][i] = '#'
            ret[2][n - 1 - i] = '#'

    else:
        for i in range(1, n - 1):
            if k < 2:
                break
            k -= 2
            ret[1][i] = '#'
            ret[2][i] = '#'
    # print('YES')
    pass
    for i in range(4):
        # print(''.join(ret[i]))
        pass


def main(n):
    k = n
    solution(n, k)


if __name__ == "__main__":
    main(10)