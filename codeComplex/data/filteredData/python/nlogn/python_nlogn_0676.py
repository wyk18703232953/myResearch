def main(n):
    # Interpret n as the length of arrays b and g, and also set m = n.
    # Ensure n >= 2 to avoid index issues in the original logic.
    if n < 2:
        n = 2
    m = n

    # Deterministic data generation for b and g:
    # b is a non-decreasing list with smaller values
    b = [i % 5 for i in range(n)]            # values from 0 to 4, repeated
    # g is a non-decreasing list with larger values
    g = [i % 7 + 3 for i in range(n)]        # values from 3 to 9, repeated

    b.sort()
    g.sort()

    if b[-1] > g[0]:
        # print(-1)
        pass
        return
    if b[-1] == g[0]:
        # print(sum(g) + m * (sum(b) - b[-1]))
        pass
        return
    if n == 1:
        # print(-1)
        pass
        return
    # print(sum(g) + b[-1] + b[-2] * (m - 1) + m * (sum(b) - b[-1] - b[-2]))
    pass
if __name__ == "__main__":
    main(10)