def main(n):
    # Interpret n as the number of test cases
    t = n
    results = []
    for case in range(1, t + 1):
        # For each test case, define ladder length equal to case index + 2 (>=2)
        length = case + 2
        # Generate a deterministic array of size 'length'
        # Values increase with index to keep structure similar to sorted input
        a = [(i * 2 + case) for i in range(length)]
        a.sort()
        results.append(str(min(a[-2] - 1, length - 2)))
    # print("\n".join(results))
    pass
if __name__ == "__main__":
    main(5)