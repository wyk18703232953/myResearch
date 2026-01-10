def main(n):
    # Interpret n as the array length; scale m and k deterministically from n
    if n <= 0:
        return
    # Generate a deterministic non-increasing array 'a' of length n
    # Example pattern: a[i] = (n - i) % 10 + 1 to keep values small but non-trivial
    a = [((n - i) % 10) + 1 for i in range(n)]
    a.sort(reverse=True)

    # Define m and k deterministically as functions of n
    # Ensure m > 0 and 0 <= k < m in general interesting cases
    m = 5 * n + 7
    k = (2 * n) // 3

    if k >= m:
        print(0)
    else:
        curr = k
        count = 0
        for i in range(n):
            curr += a[i] - 1
            count += 1
            if curr >= m:
                break
        if curr >= m:
            print(count)
        else:
            print(-1)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)