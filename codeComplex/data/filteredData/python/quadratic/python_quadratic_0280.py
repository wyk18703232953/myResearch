def main(n):
    # Interpret n as the size of both sequences a and b
    m = n

    # Deterministically generate sequences:
    # a: [0, 1, 2, ..., n-1]
    # b: [n//2, n//2+1, ..., n//2 + m -1]
    a = list(range(n))
    b = list(range(n // 2, n // 2 + m))

    # Core logic from original program
    for x in a:
        if x in b:
            # print(x, end=' ')
            pass
if __name__ == "__main__":
    main(10)