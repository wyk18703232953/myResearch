def main(n):
    # Interpret n as the size parameter: number of key-value pairs in each dictionary
    # Generate deterministic data for d1 and d2
    d1 = {}
    d2 = {}

    # First dictionary: keys 0..n-1, values = i % 7 + i // 3
    for i in range(n):
        a = i
        x = (i % 7) + (i // 3)
        d1[a] = x

    # Second dictionary: keys shifted and overlapped, values = (2*i) % 9 + i // 2
    m = n
    for i in range(m):
        b = i // 2  # ensures overlap and some collisions
        y = (2 * i) % 9 + (i // 2)
        d2[b] = y

    ans = 0
    for key in set(d1.keys()) | set(d2.keys()):
        ans += max(d1.get(key, 0), d2.get(key, 0))
    return ans


if __name__ == "__main__":
    # Example deterministic call for testing / timing
    result = main(10**4)
    # print(result)
    pass