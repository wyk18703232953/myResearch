def main(n):
    # Interpret n as:
    # n = length of array l
    # m = number of queries, choose m = n for scalability
    m = n

    # Deterministic construction of l (size n)
    # Example pattern: l[i] = (i * 2 + 1) % (n + 3)
    l = [(i * 2 + 1) % (n + 3) for i in range(n)]

    # Core logic from original code
    odd = 0
    for i in range(n):
        for j in range(i, n):
            if l[i] > l[j]:
                odd ^= 1

    # Deterministic construction of m queries
    # Construct intervals covering various ranges:
    # ll from 1 to n, r = min(n, ll + (i % max(1, n//2)))
    queries = []
    for i in range(m):
        ll = (i % n) + 1
        length = (i // 2) % max(1, n)
        r = ll + length
        if r > n:
            r = n
        if ll > r:
            ll, r = r, ll
        queries.append((ll, r))

    ans = []
    for ll, r in queries:
        k = r - ll + 1
        if (k * (k - 1) // 2) % 2:
            odd ^= 1
        ans.append("odd" if odd else "even")

    # For experimentation, we return the result instead of printing
    return ans


if __name__ == "__main__":
    # Example deterministic call for testing / benchmarking
    result = main(10)
    for line in result:
        # print(line)
        pass