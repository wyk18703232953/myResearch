def main(n):
    # Deterministic generation of U and Ar based on n
    # U controls the maximum allowed difference Ar[R] - Ar[i]
    U = n // 2 + 1
    # Generate a strictly increasing sequence so that Ar[R+1] - Ar[i] is meaningful
    # Example: quadratic growth to avoid too many equal differences
    Ar = [i * i + i for i in range(n)]

    R = 0
    ans = -1.0
    for i in range(n):
        while R + 1 < n and Ar[R + 1] - Ar[i] <= U:
            R += 1
        if i + 1 < R:
            ans = max((Ar[R] - Ar[i + 1]) / (Ar[R] - Ar[i]), ans)
    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(10)