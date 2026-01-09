def main(n):
    # Interpret n as the length of the string and the window size k.
    # To mimic multiple test cases, we can use two test cases with related sizes.
    # First test case: use k = n // 2 (at least 1)
    # Second test case: use k = max(1, n // 3)
    if n <= 0:
        return

    def generate_string(length):
        # Deterministically generate a string of 'R', 'G', 'B' with pattern
        chars = ['R', 'G', 'B']
        return ''.join(chars[i % 3] if (i // 3) % 2 == 0 else chars[(2 - i) % 3] for i in range(length))

    def solve_case(n, k, a):
        rgb = [0] * n
        gbr = [0] * n
        brg = [0] * n

        for i in range(n):
            if i % 3 == 0:
                if a[i] != "R":
                    rgb[i] += 1
            if i % 3 == 1:
                if a[i] != "G":
                    rgb[i] += 1
            if i % 3 == 2:
                if a[i] != "B":
                    rgb[i] += 1

        for i in range(n):
            if i % 3 == 0:
                if a[i] != "G":
                    gbr[i] += 1
            if i % 3 == 1:
                if a[i] != "B":
                    gbr[i] += 1
            if i % 3 == 2:
                if a[i] != "R":
                    gbr[i] += 1

        for i in range(n):
            if i % 3 == 0:
                if a[i] != "B":
                    brg[i] += 1
            if i % 3 == 1:
                if a[i] != "R":
                    brg[i] += 1
            if i % 3 == 2:
                if a[i] != "G":
                    brg[i] += 1

        for i in range(1, n):
            rgb[i] += rgb[i - 1]
            brg[i] += brg[i - 1]
            gbr[i] += gbr[i - 1]

        ans = 999999999
        for i in range(k - 1, n):
            if i - k == -1:
                ans = min(ans, rgb[i], gbr[i], brg[i])

            else:
                ans = min(ans,
                          rgb[i] - rgb[i - k],
                          gbr[i] - gbr[i - k],
                          brg[i] - brg[i - k])
        # print(ans)
        pass

    # First test case
    k1 = max(1, n // 2)
    a1 = generate_string(n)
    solve_case(n, k1, a1)

    # Second test case
    k2 = max(1, n // 3)
    a2 = generate_string(n)
    solve_case(n, k2, a2)


if __name__ == "__main__":
    main(10)