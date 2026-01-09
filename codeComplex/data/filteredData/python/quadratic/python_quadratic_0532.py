def main(n):
    # Interpret n as both n and m for scalability:
    # total length of arrays a and t will be n + m = 2n
    if n <= 0:
        return

    # Deterministically define n and m
    m = n

    # Generate array t of length n + m with exactly m ones
    # Pattern: first m positions are 1, remaining n are 0
    t = [1] * m + [0] * n

    # Generate array a of length n + m with deterministic values
    # For simplicity, a[i] = i
    a = [i for i in range(n + m)]

    ans = [0] * m
    p = []
    for i in range(n + m):
        if t[i] == 1:
            p.append(i)

    ans[0] = p[0]
    for i in range(m):
        if i == m - 1:
            ans[i] += n + m - p[i] - 1

        else:
            for j in range(p[i] + 1, p[i + 1]):
                if a[j] - a[p[i]] <= a[p[i + 1]] - a[j]:
                    ans[i] += 1

                else:
                    ans[i + 1] += 1

    # print(' '.join(map(str, ans)))
    pass
if __name__ == "__main__":
    main(10)