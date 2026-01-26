def ask(x, arr, n):
    # print('? %d' % x)
    pass
    # original: x = int(input())
    # deterministic replacement: return value based on predefined array
    return arr[(x - 1) % n]

def main(n):
    # Ensure n is even because original code uses t = n // 2 and expects certain parity
    if n < 2:
        n = 2
    if n % 2 == 1:
        n += 1

    # Deterministically generate array values based on n
    # Example pattern: arr[i] = (i * 3) % 1000, 1-based indexing mapped to 0-based
    arr = [(i * 3) % 1000 for i in range(1, n + 1)]

    t = n // 2
    if t & 1:
        # print('! -1')
        pass
        return

    l = 1
    r = n
    while l < r:
        mid = (l + r) >> 1
        if ask(mid, arr, n) >= ask((mid + t - 1) % n + 1, arr, n):
            r = mid

        else:
            l = mid + 1
    # print('! %d' % l)
    pass
if __name__ == "__main__":
    main(1000)