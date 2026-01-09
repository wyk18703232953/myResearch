n,m=10,5

def main(n):
    m = max(1, n // 2)
    x = [i for i in range(n)]
    y = [(i * 2) % n for i in range(m)]
    l = []
    for i in range(m):
        for j in range(n):
            if y[i] == x[j]:
                l.append(j)
    # print(' '.join(map(str, [x[i] for i in sorted(l)])))
    pass
if __name__ == "__main__":
    main(n)