def main(n):
    # Deterministically generate a string a of length n consisting of 'T' and 'H'
    # Example pattern: positions with even index are 'T', odd index are 'H'
    a = ''.join('T' if i % 2 == 0 else 'H' for i in range(n))

    b = a.count('T')
    c = -1
    for i in range(n):
        d = 0
        for j in range(b):
            d += int(a[(i + j) % n] == 'H')
        if c == -1 or d < c:
            c = d
    # print(c)
    pass
if __name__ == "__main__":
    main(10)