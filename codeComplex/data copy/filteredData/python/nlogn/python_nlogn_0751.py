def main(n):
    # Generate deterministic input of size n
    # Original input: n, followed by n integers (array a)
    # Here we construct a as a simple deterministic sequence depending on n
    a = [(i // 2) for i in range(n)]
    a = sorted(a)

    bal = 0
    if a.count(0) > 1:
        # print('cslnb')
        pass
        return
    if n - len(set(a)) > 1:
        # print('cslnb')
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
    if n == 1:
        # print('cslnb' if not a[0] % 2 else 'sjfnb')
        pass
        return

    for i in range(n):
        bal += a[i] - i
    # print('sjfnb' if bal % 2 else 'cslnb')
    pass
if __name__ == "__main__":
    # Example call for time complexity experiments
    main(10)