def main(n):
    # n is the size of the permutation a: a is [1, 2, ..., n]
    a = list(range(1, n + 1))
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

    print(''.join(winners))


if __name__ == "__main__":
    main(10)