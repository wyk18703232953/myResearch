def rotate_90(a):
    b = []
    for x in range(len(a)):
        l = []
        for y in range(len(a) - 1, -1, -1):
            l.append(a[y][x])
        b.append(l)
    return b

def flip(a):
    b = []
    for x in range(len(a)):
        l = []
        for y in range(len(a) - 1, -1, -1):
            l.append(a[x][y])
        b.append(l)
    return b

def main(n):
    if n <= 0:
        print("no")
        return

    l = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(chr(ord('a') + (i + j) % 26))
        l.append(row)

    l2 = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(chr(ord('a') + (i * 2 + j * 3) % 26))
        l2.append(row)

    d = 'no'
    for i in range(4):
        l = rotate_90(l)
        if l == l2:
            d = 'yes'
    l = flip(l)
    for i in range(4):
        l = rotate_90(l)
        if l == l2:
            d = 'yes'
    print(d)

if __name__ == "__main__":
    main(5)