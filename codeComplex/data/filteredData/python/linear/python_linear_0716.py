def main(n):
    # Deterministically generate input array 'a' of length n
    # Example: a[i] = (i + 1) * 3
    a = [(i + 1) * 3 for i in range(n)]

    ans = float('inf')
    for i in range(n):
        denom = max(i, n - i - 1)
        if denom > 0:
            ans = min(ans, a[i] // denom)

    if ans == float('inf'):
        ans = 0
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)