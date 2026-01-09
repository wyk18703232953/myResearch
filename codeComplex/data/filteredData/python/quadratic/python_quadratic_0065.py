def main(n):
    # n: length of nums
    # Deterministic generation of nums
    nums = [(i * 3 + 1) % (n + 5) for i in range(n)]

    counts = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                counts += 1

    ans = counts % 2
    ans_tmp = []

    # Define m as a deterministic function of n
    m = max(1, n // 2)

    # Generate m deterministic queries [l, r] within [0, n-1]
    # Use 1-based indexing to mirror the original problem style
    for i in range(1, m + 1):
        l = (i * 2 - 1) % n + 1
        r = (i * 3) % n + 1
        if l > r:
            l, r = r, l

        tmp = r - l + 1
        tmp_count = (tmp * (tmp - 1) // 2)
        if tmp_count % 2 == 1:
            ans = (ans + 1) % 2
        ans_tmp.append(ans)

    for i in range(m):
        ans = ans_tmp[i]
        if ans % 2 == 1:
            # print("odd")
            pass

        else:
            # print("even")
            pass
if __name__ == "__main__":
    main(10)