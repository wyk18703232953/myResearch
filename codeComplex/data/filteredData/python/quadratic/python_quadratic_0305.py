def main(n):
    a = list(range(1, n + 1))
    r = 0
    while a:
        c = a[0]
        del a[0]
        if not a:
            break
        for i in range(len(a)):
            if c == a[i]:
                break
        del a[i]
        r += i
    # print(r)
    pass
if __name__ == "__main__":
    main(10)