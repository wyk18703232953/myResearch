def main(n):
    a = []
    for i in range(1, n + 1):
        l = i
        r = 2 * i
        a.append([l, -r, i])
    a.sort()
    ma = a[0][1]
    nma = a[0][2]
    for i in range(1, n):
        if a[i][1] >= ma:
            return a[i][2], nma
        else:
            ma = a[i][1]
            nma = a[i][2]
    return -1, -1

if __name__ == "__main__":
    print(main(5))