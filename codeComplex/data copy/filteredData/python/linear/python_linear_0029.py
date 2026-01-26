def main(n):
    # Deterministically generate a string a of length n composed of 'T' and 'H'
    # Pattern: positions divisible by 3 are 'T', others are 'H'
    a = ''.join('T' if i % 3 == 0 else 'H' for i in range(n)) if n > 0 else ''

    b = a.count('T')
    c = -1
    for i in range(n):
        d = 0
        for j in range(b):
            d += int(a[(i + j) % n] == 'H')
        if c == -1 or d < c:
            c = d
    return c


if __name__ == "__main__":
    # Example: run main with a chosen n and print the result
    result = main(10)
    # print(result)
    pass