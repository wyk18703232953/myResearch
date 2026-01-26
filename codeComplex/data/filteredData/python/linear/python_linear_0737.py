def main(n):
    # n controls both initial array size and number of queries
    # array length at least 2 to keep original behavior meaningful
    size = max(2, n)
    q = n

    # deterministic generation of nums: simple arithmetic sequence
    nums = [i + 1 for i in range(size)]

    m = max(nums)
    ab = []
    while nums[0] < m:
        ab.append([nums[0], nums[1]])
        if nums[0] > nums[1]:
            nums.append(nums.pop(1))

        else:
            nums.append(nums.pop(0))

    outputs = []
    for i in range(q):
        mj = i + 1
        if mj <= len(ab):
            a, b = ab[mj - 1]

        else:
            idx = (mj - len(ab) - 1) % (len(nums) - 1) + 1
            a, b = m, nums[idx]
        outputs.append(f"{a} {b}")
    return outputs


if __name__ == "__main__":
    # example: run with n = 10 and print results
    result = main(10)
    for line in result:
        # print(line)
        pass