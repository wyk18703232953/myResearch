def main(n):
    # Interpret n as: number of rows = n, number of columns = m = max(1, n)
    # Generate a deterministic n x m matrix 'a' of integers
    global a, m
    m = max(1, n)
    a = [[(i * 31 + j * 7) % 1000 for j in range(m)] for i in range(n)]

    def ok(here):
        have = {}
        for j in range(n):
            b = a[j]
            s = []
            for x in b:
                if x >= here:
                    s.append('1')
                else:
                    s.append('0')
            key = int(''.join(s), 2)
            have[key] = j

        full_mask = (1 << m) - 1
        # Original code loops only up to 300, keep that behavior
        limit = 300
        for i in range(limit):
            for j in range(limit):
                if (i | j) == full_mask and i in have and j in have:
                    return (have[i] + 1, have[j] + 1)
        return -1

    low = 0
    high = 10**9
    ans = (-1, -1)
    while low <= high:
        mid = low + (high - low) // 2
        here = ok(mid)
        if here != -1:
            ans = here
            low = mid + 1
        else:
            high = mid - 1

    # Return instead of printing, to be suitable for experiments
    return ans


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    result = main(10)
    print(result)