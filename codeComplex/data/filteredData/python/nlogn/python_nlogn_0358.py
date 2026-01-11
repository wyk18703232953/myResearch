def main(n):
    # n is the length of the array
    if n <= 0:
        return
    # Deterministic generation of array a of length n
    # Example pattern: a[i] = i for i in range(n)
    a = list(range(n))

    d = {}
    power = [2 ** i for i in range(31)]
    ans = []
    for i in a:
        d[i] = 0

    found = False
    for num in d.keys():
        for p in power:
            if num + p in d:
                ans = [num, num + p]
                if num + p + p in d:
                    # print(3)
                    pass
                    ans.append(num + p + p)
                    # print(*ans)
                    pass
                    found = True
                    break
        if found:
            break

    if not found:
        if ans:
            # print(2)
            pass
            # print(*ans)
            pass

        else:
            # print(1)
            pass
            # print(a[0])
            pass
if __name__ == "__main__":
    main(10)