def main(n):
    # n controls the size of the single test case: length of string a, and k = max(1, n//2)
    if n <= 0:
        return
    t = 1  # number of test cases, fixed to 1 for deterministic scaling
    results = []
    for _ in range(t):
        length = n
        k = max(1, n // 2)
        # Generate deterministic string a of length n over 'R', 'G', 'B'
        base = "RGB"
        a = "".join(base[i % 3] for i in range(length))

        rgb = [0 for _ in range(length)]
        gbr = [0 for _ in range(length)]
        brg = [0 for _ in range(length)]

        for i in range(length):
            if i % 3 == 0:
                if a[i] != "R":
                    rgb[i] += 1
            if i % 3 == 1:
                if a[i] != "G":
                    rgb[i] += 1
            if i % 3 == 2:
                if a[i] != "B":
                    rgb[i] += 1

        for i in range(length):
            if i % 3 == 0:
                if a[i] != "G":
                    gbr[i] += 1
            if i % 3 == 1:
                if a[i] != "B":
                    gbr[i] += 1
            if i % 3 == 2:
                if a[i] != "R":
                    gbr[i] += 1

        for i in range(length):
            if i % 3 == 0:
                if a[i] != "B":
                    brg[i] += 1
            if i % 3 == 1:
                if a[i] != "R":
                    brg[i] += 1
            if i % 3 == 2:
                if a[i] != "G":
                    brg[i] += 1

        for i in range(1, length):
            rgb[i] += rgb[i - 1]
            brg[i] += brg[i - 1]
            gbr[i] += gbr[i - 1]

        ans = 999999999
        for i in range(k - 1, length):
            if i - k == -1:
                ans = min(ans, rgb[i], gbr[i], brg[i])

            else:
                ans = min(
                    ans,
                    rgb[i] - rgb[i - k],
                    gbr[i] - gbr[i - k],
                    brg[i] - brg[i - k],
                )
        results.append(ans)
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(10)