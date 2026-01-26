def main(n):
    # n is the length of the string l; we must also provide k deterministically
    if n <= 0:
        return

    # Define k as a deterministic function of n, but not exceeding n
    # This keeps the behavior non-trivial for time complexity experiments
    k = max(1, n // 2)
    if k > n:
        k = n

    # Deterministically construct the string l of length n
    # Cycle through 'a' to 'z' in a fixed pattern
    chars = []
    for i in range(n):
        c = chr(ord('a') + (i % 26))
        chars.append(c)
    l = "".join(chars)

    # Original algorithm logic
    l = sorted(l)
    ans = l[0]
    s = ord(l[0])
    index = 0
    for j in range(1, n):
        if len(ans) < k:
            if ord(l[j]) - ord(l[index]) > 1:
                ans = ans + l[j]
                s = s + ord(l[j])
                index = j

        else:
            break
    if len(ans) == k:
        s = s - 96 * k
        # print(s)
        pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    # Example deterministic calls for experimental runs
    main(5)
    main(10)
    main(100)