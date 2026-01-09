def main(n):
    a = [i for i in range(n)]
    fl = False
    ans = True
    for i in range(n - 1):
        if a[i + 1] > a[i]:
            if fl:
                ans = False

        else:
            fl = True
    if ans:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)