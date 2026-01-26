def ask(x, arr, n):
    # original interactive ask(x) is replaced by deterministic access to arr
    return arr[(x - 1) % n]

def main(n):
    # Ensure n is even because original code uses t = n // 2 and expects some structure
    if n < 2:
        return

    # Deterministically generate an array arr[1..n] (1-based logical indexing)
    # Example pattern: first half increasing, second half offset by constant
    # This ensures some structure but is fully deterministic.
    arr = [(i + (i // (n // 2))) for i in range(1, n + 1)]

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
    # Example deterministic call; adjust n as needed for experiments
    main(10)