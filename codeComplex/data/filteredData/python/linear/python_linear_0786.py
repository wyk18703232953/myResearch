def is_winning_state(nims, n):
    keys = set(nims)
    counts = dict.fromkeys(keys, 0)
    for nim in nims:
        counts[nim] += 1
    if 0 in keys and counts[0] > 1:
        return True
    lose_count = 0
    for k in keys:
        if counts[k] > 2:
            return True
        if counts[k] > 1 and (k - 1) in keys and counts[k - 1] > 0:
            return True
        if counts[k] > 1:
            lose_count += 1
    if lose_count > 1:
        return True
    return False


def main(n):
    if n < 0:
        n = 0
    n_int = n

    if n_int == 0:
        n_int = 1

    nims = [(i * 2) // 3 for i in range(n_int)]

    if is_winning_state(nims, n_int):
        print('cslnb')
    else:
        x = sum(nims) - (n_int * (n_int - 1)) // 2
        if x % 2 == 0:
            print('cslnb')
        else:
            print('sjfnb')


if __name__ == "__main__":
    main(10)