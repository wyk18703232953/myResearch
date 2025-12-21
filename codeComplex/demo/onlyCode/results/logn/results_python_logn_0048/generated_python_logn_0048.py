def main(n):
    l = n
    r = 2 * n + 1
    r_bin = bin(r)[2:]
    l_bin = bin(l)[2:]
    r_rev = r_bin[::-1]
    l_rev = l_bin[::-1]
    if l_rev == r_rev:
        return 0
    l_rev += '0' * (len(r_rev) - len(l_rev))
    p = -1
    for i in range(len(r_rev)):
        if r_rev[i] != l_rev[i]:
            p = i
    a = '1' * p + '0'
    b = '0' * p + '1'
    return int(a, 2) ^ int(b, 2)

if __name__ == "__main__":
    print(main(10))