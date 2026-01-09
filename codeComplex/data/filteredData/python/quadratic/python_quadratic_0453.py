def main(n):
    # Deterministic construction of input:
    # n: size of the array
    # a: a permutation of 1..n in a fixed pattern
    # Example pattern: cyclic shift by 1.
    if n <= 0:
        return ""
    a = [((i + 1) % n) + 1 for i in range(n)]

    indx = [0] * n
    winners = [''] * n

    for i, ai in enumerate(a):
        indx[ai - 1] = i

    for ai in range(n, 0, -1):
        i = indx[ai - 1]
        can_win = False

        for j in range(i + ai, n, ai):
            if a[j] > ai and winners[j] == 'B':
                can_win = True
                break

        if not can_win:
            for j in range(i - ai, -1, -ai):
                if a[j] > ai and winners[j] == 'B':
                    can_win = True
                    break

        if can_win:
            winners[i] = 'A'

        else:
            winners[i] = 'B'

    result = ''.join(winners)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)