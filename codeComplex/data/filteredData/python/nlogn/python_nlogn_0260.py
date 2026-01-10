def main(n):
    l = []
    for i in range(n):
        a = i + 1
        b = (i * 2 + 3) % (n + 5)
        l.append((a, -b, i + 1))
    l = sorted(l)
    for i in range(1, n):
        if l[i][1] >= l[i - 1][1]:
            print(l[i][2], l[i - 1][2])
            break
    else:
        print(-1, -1)

if __name__ == "__main__":
    main(10)