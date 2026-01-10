def main(n):
    # Interpret n as the size of the list l
    # Deterministically generate k and l based on n
    # Ensure 1 <= k <= n
    if n <= 0:
        return

    # Define k as a deterministic function of n
    # For example: k cycles between 1 and n with a simple rule
    k = (n // 3) + 1
    if k > n:
        k = n

    # Generate a sorted list l of length n deterministically
    # Make gaps vary but deterministic
    l = [i * (i % 5 + 1) for i in range(n)]

    cost = l[n - 1] - l[0]
    if k == 1:
        print(cost)
    else:
        diff = [0 for _ in range(n - 1)]
        for i in range(n - 1):
            diff[i] = l[i + 1] - l[i]
        diff = sorted(diff)
        diff.reverse()
        print(cost - sum(diff[:k - 1]))


if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)