def main(n):
    s = []
    for i in range(4):
        df = 0
        for k in range(n):
            # deterministically generate a line of length n consisting of '0' and '1'
            # pattern depends on i and k to emulate different boards
            l = ''.join(str((i + k + j) % 2) for j in range(n))
            for j in range(n):
                if int(l[j]) == (k + j) % 2:
                    df += 1
        s.append(df)

    nn = n * n
    ans = min(
        s[0] + s[1] + nn - s[2] + nn - s[3],
        s[0] + s[2] + nn - s[1] + nn - s[3],
        s[0] + s[3] + nn - s[1] + nn - s[2],
        s[1] + s[2] + nn - s[0] + nn - s[3],
        s[1] + s[3] + nn - s[0] + nn - s[2],
        s[2] + s[3] + nn - s[0] + nn - s[1],
    )
    # print(ans)
    pass
if __name__ == "__main__":
    main(5)