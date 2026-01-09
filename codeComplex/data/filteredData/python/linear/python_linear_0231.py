def main(n):
    # Interpret n as length of string b
    a = n
    b = ''.join('x' if (i % 3 == 0) else 'y' for i in range(a))
    s = 0
    for i in range(a - 2):
        if b[i:i + 3] == 'xxx':
            s += 1
    # print(s)
    pass
if __name__ == "__main__":
    main(10)