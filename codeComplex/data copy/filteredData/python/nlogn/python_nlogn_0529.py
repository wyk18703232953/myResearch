def main(n):
    from collections import Counter

    # Map n to problem scale:
    # - Use n as number of elements
    # - Choose a fixed k > 0
    k = 10 if n == 0 else (n % 97) + 2  # ensure k >= 2, deterministic from n

    # Generate deterministic list of integers a1 and their string forms a
    # Values grow with index but stay within a reasonable range
    a1 = [(i * i + 3 * i + 7) for i in range(n)]
    a = [str(x) for x in a1]

    dct = [Counter() for _ in range(11)]
    for i in range(n):
        dct[len(a[i])][a1[i] % k] += 1

    ans = 0
    for i in range(n):
        x = a1[i]
        for j in range(1, 11):
            x = (x * 10) % k
            if x:
                ans += dct[j][k - x]

            else:
                ans += dct[j][0]
        if not (a1[i] * (pow(10, len(a[i]), k) + 1)) % k:
            ans -= 1

    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call for testing / benchmarking
    main(1000)