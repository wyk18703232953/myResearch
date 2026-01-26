def main(n):
    # Generate deterministic input: n lines, each with 3 integers
    # Original structure:
    # n
    # a_1 b_1 c_1
    # ...
    # a_n b_n c_n
    # Here we construct them deterministically from n.
    l = []
    for i in range(n):
        # Example deterministic construction
        # You can change the pattern as long as it is deterministic and uses n, i
        a = i
        b = (i + 1) % (n + 1) if n > 0 else 0
        c = (i * 2) // (n + 1) if n > 0 else 0
        l.append(a + b + c)

    if not l:
        return

    m = l[0]
    l.sort(reverse=True)
    for i in range(len(l)):
        if m == l[i]:
            # print(i + 1)
            pass
            break


if __name__ == "__main__":
    main(10)