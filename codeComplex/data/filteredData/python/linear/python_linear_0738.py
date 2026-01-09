def main(n):
    # Interpret n as initial number of elements; also set number of queries q deterministically
    if n < 2:
        n = 2
    nums = [i + 1 for i in range(n)]
    q = n * 2

    m = max(nums)
    ab = []
    while nums[0] < m:
        ab.append([nums[0], nums[1]])
        if nums[0] > nums[1]:
            nums.append(nums.pop(1))

        else:
            nums.append(nums.pop(0))

    # Deterministic generation of q queries
    # Use a pattern that covers values <= len(ab) and > len(ab)
    queries = []
    base = len(ab)
    if base == 0:
        base = 1
    for i in range(q):
        if i % 2 == 0:
            # ensure some queries are within the prefix part
            queries.append((i % base) + 1)

        else:
            # ensure some queries are beyond the prefix part
            queries.append(base + 1 + (i // 2) % (len(nums) + q))

    for mj in queries:
        if mj <= len(ab):
            a, b = map(str, ab[mj - 1])

        else:
            idx = (mj - len(ab) - 1) % (len(nums) - 1) + 1
            a, b = map(str, (m, nums[idx]))
        # print(a + " " + b)
        pass
if __name__ == "__main__":
    main(10)