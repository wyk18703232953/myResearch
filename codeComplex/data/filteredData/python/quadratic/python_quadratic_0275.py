def main(n):
    # Interpret n as the size of lists c and d
    a = n

    # Deterministically generate c and d
    # c: [0, 1, 2, ..., n-1]
    c = [i for i in range(a)]
    # d: [n//2, n//2+1, ..., 3n//2 - 1]
    d = [i for i in range(a // 2, a // 2 + a)]

    e = []
    for i in c:
        if i in d:
            e.append(i)
    for j in e:
        # print(j, end=" ")
        pass
if __name__ == "__main__":
    main(10)