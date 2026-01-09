def main(n):
    # Map n to problem parameters:
    # - number of elements: n
    # - initial m: n * 10 (arbitrary deterministic scaling)
    # - arrays a, b of length n with simple deterministic values
    m = n * 10
    a = [i % 7 + 1 for i in range(1, n + 1)]
    b = [i % 5 + 2 for i in range(1, n + 1)]

    low = 1.0
    high = 1000000000.0
    ans = -1.0
    eps = 0.000001

    while low <= high:
        if high - low < eps:
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
            high = mid - eps

        else:
            low = mid + eps

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

    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)