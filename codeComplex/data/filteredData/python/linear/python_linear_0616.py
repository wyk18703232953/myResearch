def main(n):
    # n controls the size of the permutation arrays a and b
    if n <= 0:
        return

    # Generate a deterministic permutation a of 1..n
    # Example: a[i] = (i*3) % n + 1 ensures a permutation when gcd(3, n) == 1
    # To keep it deterministic for all n, we can use a simple pattern:
    a = list(range(1, n + 1))

    # Generate b as another deterministic permutation of 1..n
    # For variety but still deterministic, we reverse a
    b = a[::-1]

    max_val = 2 * 10**5 + 1
    if n > max_val - 1:
        # Cap since original array pos_of has fixed size
        # This mirrors original constraints behavior
        n_eff = max_val - 1
        a = a[:n_eff]
        b = b[:n_eff]
    else:
        n_eff = n

    pos_of = [-1 for _ in range(max_val)]
    for i, ele in enumerate(a):
        if ele < max_val:
            pos_of[ele] = i + 1

    current_pos = 0
    ans = []
    for x in b:
        if x < max_val and pos_of[x] > current_pos:
            ans.append(pos_of[x] - current_pos)
            current_pos = pos_of[x]
        else:
            ans.append(0)

    print(" ".join(str(x) for x in ans))


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(10)