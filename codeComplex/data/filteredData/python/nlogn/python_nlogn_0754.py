def main(n):
    # Interpret n as the number of test cases and also scale of each test
    t = n
    results = []
    for case_idx in range(t):
        # For each test case, define array size depending on case index and n
        size = max(2, (case_idx + 2))  # ensure at least 2 elements
        # Deterministically generate array values based on n and case index
        arr = [(n + case_idx * 3 + i * 2) for i in range(size)]
        arr.sort(reverse=True)
        res = min(arr[1] - 1, len(arr) - 2)
        results.append(res)
    # For time complexity experiments, we still print results
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(5)