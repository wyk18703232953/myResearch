def main(n):
    # n: input size, length of array a
    if n <= 0:
        return
    # Deterministic data generation
    # Example: a[i] = i for i in range(n), matching increasing integers
    a = [i for i in range(n)]
    s = set(a)
    a.sort()
    ans = []
    for i in range(n):
        for j in range(31):
            tmp = [a[i]]
            x = a[i] + (1 << j)
            y = a[i] + (1 << (j + 1))
            if x in s:
                tmp.append(x)
            if y in s:
                tmp.append(y)
            if len(tmp) > 1:
                if len(ans) == 0:
                    ans.append(tmp)
                else:
                    if len(tmp) > len(ans[0]):
                        ans[0] = tmp
    if len(ans) == 0:
        print(1)
        print(a[0])
        return
    if len(ans[0]) == 2:
        print(2)
        print(ans[0][0], ans[0][1])
        return
    if len(ans[0]) == 3:
        print(3)
        print(ans[0][0], ans[0][1], ans[0][2])
        return


if __name__ == "__main__":
    # example deterministic call
    main(10)