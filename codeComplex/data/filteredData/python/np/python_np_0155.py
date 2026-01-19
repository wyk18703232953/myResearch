def main(n):
    # Map n to a problem size
    # Use n as number of problems; define l, r, x deterministically from n
    if n <= 0:
        return 0

    # Generate c as a deterministic list of length n
    # Example: c[i] = i + 1
    c = [i + 1 for i in range(n)]

    # Define l, r, x based on n and c in a deterministic way
    total = sum(c)
    l = total // 4
    r = (3 * total) // 4
    x = max(1, n // 4)

    ans = 0
    for bit in range(2, 1 << n):
        probs = []
        t = 0
        for i in range(n):
            if bit & (1 << i):
                probs.append(c[i])
                t += c[i]

        if not probs:
            continue

        a = min(probs)
        b = max(probs)

        if l <= t <= r and abs(a - b) >= x:
            ans += 1
    return ans


if __name__ == "__main__":
    # Example deterministic call
    result = main(10)
    print(result)