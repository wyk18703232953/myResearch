def check(x, y):
    return ''.join([''.join(s) for s in x]) == ''.join([''.join(s) for s in y])

def main(n):
    re = max(1, n)
    a = []
    for i in range(re):
        row = [chr(ord('a') + (i + j) % 26) for j in range(re)]
        a.append(row)
    b = []
    for i in range(re):
        row = [chr(ord('a') + (i * 2 + j * 3) % 26) for j in range(re)]
        b.append(row)

    for _ in range(4):
        for _ in range(2):
            if check(a, b):
                # print('Yes')
                pass
                return
            b = b[::-1]
        for _ in range(2):
            if check(a, b):
                # print('Yes')
                pass
                return
            b = [s[::-1] for s in b]
        c = [['' for _ in range(re)] for _ in range(re)]
        for t in range(re):
            for u in range(re):
                c[t][u] = b[u][re - t - 1]
        b = c[:]
        if check(a, b):
            # print('Yes')
            pass
            return
    # print('No')
    pass
if __name__ == "__main__":
    main(5)