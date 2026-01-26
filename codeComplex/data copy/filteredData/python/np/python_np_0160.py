def main(n):
    # Map n to problem parameters deterministically
    # Ensure n is at least 1
    if n < 1:
        n = 1

    # Define bounds and difficulty parameter based on n
    # l: lower bound of sum, r: upper bound of sum, x: minimum difficulty spread
    l = n
    r = 2 * n * (n + 1) // 2  # large enough upper bound
    x = max(1, n // 4)

    # Generate nums deterministically: 1, 2, ..., n
    nums = list(range(1, n + 1))

    ans = 0
    length = n

    def recurse(i, sum_val, cnt):
        nonlocal ans
        if i == length:
            if not cnt:
                return
            if l <= sum_val <= r and abs(cnt[-1] - cnt[0]) >= x:
                ans += 1
            return
        # Exclude nums[i]
        recurse(i + 1, sum_val, cnt)
        # Include nums[i]
        cnt.append(nums[i])
        recurse(i + 1, sum_val + nums[i], cnt)
        cnt.pop()

    recurse(0, 0, [])
    print(ans)


if __name__ == "__main__":
    main(10)