def main(n):
    # Interpret n as the number of elements in arrays a and b
    if n <= 0:
        return

    # Deterministic generation of m, a, b based on n
    m = n * 10
    a = [i % 9 + 1 for i in range(1, n + 1)]
    b = [(i * 2) % 9 + 1 for i in range(1, n + 1)]

    low = 1.0
    high = 1000000000.0
    ans = -1.0

    # Binary search over possible answer
    while low <= high:
        if high - low < 0.000001:
            low = high
        mid = low + (high - low) / 2.0
        try_val = mid
        init_wt = m + try_val
        isPossible = True

        for i in range(n):
            req1 = init_wt / a[i]
            try_val -= req1
            if try_val <= 0:
                isPossible = False
                break
            j = (i + 1) % n
            init_wt -= req1
            req2 = init_wt / b[j]
            try_val -= req2
            if try_val < 0 or (i < n - 1 and try_val == 0):
                isPossible = False
                break
            init_wt -= req2

        if isPossible:
            ans = mid
            high = mid - 0.000001
        else:
            low = mid + 0.000001

    if ans == -1.0:
        isPossible = True
        try_val = 1000000000.000001
        init_wt = m + try_val
        for i in range(n):
            req1 = init_wt / a[i]
            try_val -= req1
            if try_val <= 0:
                isPossible = False
                break
            j = (i + 1) % n
            init_wt -= req1
            req2 = init_wt / b[j]
            try_val -= req2
            if try_val < 0 or (i < n - 1 and try_val == 0):
                isPossible = False
                break
            init_wt -= req2
        if isPossible:
            ans = 1000000000.0

    print(ans)


if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(10)