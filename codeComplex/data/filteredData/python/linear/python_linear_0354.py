def main(n):
    # Generate a deterministic numeric string s of length n
    # Digits cycle from 0 to 9
    s = ''.join(str(i % 10) for i in range(n))
    n_len = len(s)
    l = [[0, 0, 0] for _ in range(n_len)]
    ans = 0
    if n_len > 0:
        x = int(s[0]) % 3
        if x == 0:
            ans += 1

        else:
            l[0][x] = 1
        for i in range(1, n_len):
            x = int(s[i]) % 3
            if x == 0:
                ans += 1
                continue
            if l[i - 1][3 - x] > 0:
                ans += 1
                l[i][3 - x] = 0
                l[i][x] = 0

            else:
                if l[i - 1][x] != 0:
                    l[i][1] = 1
                    l[i][2] = 1

                else:
                    l[i][x] = 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)