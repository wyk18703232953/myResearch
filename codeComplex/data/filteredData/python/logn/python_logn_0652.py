def main(n):
    # n controls the "input size" by defining x[0]
    # Construct a deterministic target based on n and a mid derived from n
    # to ensure the algorithm runs a non-trivial binary search.

    x0 = n
    if x0 <= 0:
        # print(0)
        pass
        return

    # Choose a deterministic mid in [0, x0-1]
    mid = x0 // 2

    # Compute target as in the original logic:
    # sum_mid - ans1 where sum_mid = mid*(mid+1)//2 and ans1 = x0 - mid
    sum_mid = mid * (mid + 1) // 2
    ans1 = x0 - mid
    target = sum_mid - ans1

    x = [x0, target]

    start = 0
    end = x[0] - 1

    target = x[1]

    ans = 0

    while start <= end:
        mid = (start + end) // 2
        s = mid * (mid + 1) // 2
        ans1 = x[0] - mid

        if s - ans1 == target:
            ans = ans1
            break
        elif s - ans1 > target:
            end = mid - 1

        else:
            start = mid + 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)