def main(n):
    # Interpret n as the length of array a, with values in [1, n]
    m = n
    a = [(i % n) + 1 for i in range(m)]
    b = [0] * n
    for i in a:
        b[i - 1] += 1
    b.sort()
    # print(b[0])
    pass
if __name__ == "__main__":
    main(10)