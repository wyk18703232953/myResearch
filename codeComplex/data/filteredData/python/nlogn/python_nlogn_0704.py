def main(n):
    # Generate deterministic test data based on n
    # We map n to:
    # - array length = n
    # - construct array with some repeated and zero elements deterministically
    a = []
    for i in range(n):
        # Deterministic pattern with possible duplicates and zeros
        # Values are small relative to n to keep behavior interesting
        val = (i // 2) % max(1, n // 3 + 1)
        a.append(val)

    a = sorted(a)
    tmp = 0
    if a.count(0) > 1:
        # print('cslnb')
        pass
        return
    if n - len(set(a)) > 1:
        # print('cslnb')
        pass
        return
    if n == 1:
        # print('cslnb' if not a[0] % 2 else 'sjfnb')
        pass
        return
    if n - len(set(a)) == 1:
        for i in range(1, n):
            if a[i] == a[i - 1]:
                if a[i] - 1 in a:
                    # print('cslnb')
                    pass
                    return
                break
    for i in range(n):
        tmp += a[i] - i
    # print('cslnb' if not tmp % 2 else 'sjfnb')
    pass
if __name__ == "__main__":
    # Example deterministic calls for experimentation
    for size in [1, 2, 5, 10, 20, 50]:
        main(size)