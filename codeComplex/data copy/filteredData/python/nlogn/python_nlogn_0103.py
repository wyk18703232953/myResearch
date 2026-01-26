def main(n):
    l = [(i * 3 + 1) % (n + 5) for i in range(n)]
    l1 = sorted(l)
    c = 0
    for i in range(n):
        if l[i] != l1[i]:
            c += 1
    if c <= 2:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)