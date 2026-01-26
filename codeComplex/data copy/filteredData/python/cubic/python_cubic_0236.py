def main(n):
    # Map n to sizes of R, G, B
    # Ensure they are at least 1
    R = max(1, n // 3)
    G = max(1, n // 3 + (1 if n % 3 > 0 else 0))
    B = max(1, n - R - G)

    # Deterministic generation of r, g, b based on R, G, B
    r = [i + 1 for i in range(R)]
    g = [2 * (i + 1) for i in range(G)]
    b = [3 * (i + 1) for i in range(B)]

    r.sort()
    g.sort()
    b.sort()

    # DP table sized by (R+1)*(G+1)*(B+1) stored in a 1D list
    size_R = R + 1
    size_G = G + 1
    size_B = B + 1

    max_area = [None] * (size_R * size_G * size_B)

    def f(i, j, k):
        # Convert (i, j, k) to a unique index in [0, size_R*size_G*size_B)
        return (i + 1) * size_G * size_B + (j + 1) * size_B + (k + 1)

    def get_max_area(i, j, k):
        temp = f(i, j, k)
        if max_area[temp] is not None:
            return max_area[temp]

        x1 = x2 = x3 = 0
        if i >= 0 and j >= 0:
            x1 = get_max_area(i - 1, j - 1, k) + r[i] * g[j]
        if i >= 0 and k >= 0:
            x2 = get_max_area(i - 1, j, k - 1) + r[i] * b[k]
        if j >= 0 and k >= 0:
            x3 = get_max_area(i, j - 1, k - 1) + g[j] * b[k]

        max_area[temp] = max(x1, x2, x3)
        return max_area[temp]

    result = get_max_area(R - 1, G - 1, B - 1)
    # print(result)
    pass
if __name__ == "__main__":
    main(6)