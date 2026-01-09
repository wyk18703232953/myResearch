def main(n):
    # n controls the scale of input: we generate a list of 14 integers
    # using a simple deterministic arithmetic pattern based on n.
    a = [((i + 1) * (n + 1)) % 20 for i in range(14)]

    mx = -1

    for i in range(14):
        b = a.copy()
        if a[i]:
            b[i], d, ans = 0, i + 1, 0
            r = (a[i] + d) // 14
            l = (a[i] + d) % 14

            if d + a[i] < 14:
                ans = sum([j + 1 for j in a[d:d + a[i]] if not (j + 1) % 2])

            else:
                for j in range(14):
                    b[j] += r
                if d > l:
                    for j in range(l, d):
                        b[j] -= 1

                else:
                    for j in range(d, d + abs(d - l)):
                        b[j] += 1
                ans = sum([p for p in b if not p % 2])
            mx = max(mx, ans)

    return mx


if __name__ == "__main__":
    # example call
    result = main(10)
    # print(result)
    pass