def main(n):
    # n is the number of elements in ti (and also used to derive other parameters)
    # Deterministically construct parameters n, a, b, c, t and list ti
    
    # Use n as given; define a, b, c, t as simple functions of n
    a = 2 * n + 1
    b = n % 7 + 1
    c = b + (n % 5)
    # Ensure t is at least as large as the largest ti plus some margin
    t = 3 * n + 10

    # Generate ti as a deterministic non-decreasing sequence within [0, t]
    # Example: arithmetic progression truncated by t
    ti = [(i * 2) % (t // 2 + 1) for i in range(n)]

    # Core logic from original solve()
    if b > c:
        ans = n * a

    else:
        ti.sort()
        ans = 0
        for i in ti:
            ans += (t - i) * (c - b) + a

    return ans


if __name__ == "__main__":
    # Example deterministic call for testing / timing
    result = main(10)
    # print(result)
    pass