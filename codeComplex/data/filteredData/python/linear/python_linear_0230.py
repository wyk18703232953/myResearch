def main(n):
    size = n
    s = "".join('x' if i % 3 == 0 else 'y' for i in range(size))

    ct = 0
    F = 0
    for i in range(size - 2):
        if s[i] == s[i + 1] and s[i + 1] == s[i + 2] and s[i] == 'x':
            ct += 1
            F = 1

    if F == 0:
        # print(0)
        pass

    else:
        # print(ct)
        pass
if __name__ == "__main__":
    main(10)