def main(n):
    # Interpret n as the length of nums, fix k deterministically as a small integer > 1
    k = 7

    # Deterministic generation of nums:
    # Create a list of n integers with varying lengths and values
    # Example pattern: numbers growing roughly linearly, with some modular variation
    nums = [(i * 1234567 + i * i) // 3 + 1 for i in range(1, n + 1)]

    counts = [{} for _ in range(11)]
    for value in nums:
        a = value
        for i in range(11):
            r = a % k
            try:
                counts[i][r] += 1
            except KeyError:
                counts[i][r] = 1
            a *= 10
    res = 0
    for i in nums:
        wo = str(i)
        le = len(wo)
        mimo = (k - (i % k)) % k
        if mimo in counts[le]:
            res += counts[le][mimo]
            if int(wo + wo) % k == 0:
                res -= 1
    return res


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    result = main(10000)
    print(result)