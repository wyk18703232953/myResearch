def main(n):
    # In the original code, the first input is an integer whose half (integer division) is used as n
    # The second input is a list of 2*n integers.
    # Here, we deterministically generate a list 'a' of length 2*n.
    size = 2 * n
    a = [(i % 7) + (i // 3) for i in range(size)]

    n_half = n
    b = [0] * n_half
    a.reverse()
    for i in a:
        b.append(i)
    mem = b[-1]
    c = 0
    for i in range(n_half - 1):
        if b[-2 - i] - c > mem:
            c = b[-2 - i] - mem
        b[-2 - i] -= c
        b[1 + i] += c
        mem = b[-2 - i]
    for i in b:
        # print(i, end=' ')
        pass
if __name__ == "__main__":
    main(5)