def main(n):
    # Interpret n as the number of test cases
    t = n

    # Deterministically generate t pairs (a, b)
    # Example: a = i + 1, b = 2*i + 3 to ensure positivity and variety
    pairs = [(i + 1, 2 * i + 3) for i in range(t)]

    results = []
    for a, b in pairs:
        if a > b:
            a, b = b, a
        ans = 0
        while a > 0:
            ans += b // a
            b %= a
            a, b = b, a
        results.append(ans)

    # For timing experiments, typically just ensure the loop runs; here we return results
    return results


if __name__ == "__main__":
    # Example fixed-scale call
    res = main(10)
    for x in res:
        # print(x)
        pass