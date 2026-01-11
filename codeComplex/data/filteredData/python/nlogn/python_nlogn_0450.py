def main(n):
    # n: length of nums
    if n < 1:
        # print(0)
        pass
        return

    # Deterministic generation of n, m, nums
    # Choose m as a value that is guaranteed to appear: middle value
    m = n // 2 if n > 1 else 0
    # Construct nums so that m appears at least once and distribution is varied but deterministic
    nums = [(i * 2) % (n + 3) for i in range(n)]
    # Ensure m is in nums by placing it at a deterministic index
    start_index = n // 3
    if start_index >= n:
        start_index = 0
    nums[start_index] = m

    n = len(nums)

    left = {}
    right = {}

    leftl = 0
    leftm = 0

    rightl = 0
    rightm = 0

    start = nums.index(m)

    ans = 1

    for i in range(start - 1, -1, -1):
        if nums[i] > m:
            leftm += 1

        else:
            leftl += 1

        if leftl == leftm:
            ans += 1
        elif leftl + 1 == leftm:
            ans += 1

        temp = leftm - leftl
        if temp in left:
            left[temp] += 1

        else:
            left[temp] = 1

    for i in range(start + 1, n, 1):
        if nums[i] > m:
            rightm += 1

        else:
            rightl += 1

        if rightl == rightm:
            ans += 1
        elif rightl + 1 == rightm:
            ans += 1

        temp = rightm - rightl
        if temp in right:
            right[temp] += 1

        else:
            right[temp] = 1

    for i in left:
        poss = -i
        if poss in right:
            ans += right[poss] * left[i]

        if poss + 1 in right:
            ans += right[poss + 1] * left[i]

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)