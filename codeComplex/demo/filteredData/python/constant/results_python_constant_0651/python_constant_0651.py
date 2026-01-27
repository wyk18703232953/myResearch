def main(n):
    from collections import defaultdict, Counter
    from copy import deepcopy

    # Deterministic data generation
    if n <= 1:
        n = 2
    c = 1
    a = [(i % (n // 2 + 1)) + 1 for i in range(n)]

    nums = defaultdict(lambda: [0])
    freq = Counter()
    minus = 0
    for i in a:
        if i == c:
            minus += 1

        else:
            freq[i] += 1
            nums[i].append(freq[i] - minus)
    tot = minus
    suff = deepcopy(nums)
    for i in nums:
        for j in range(len(nums[i]) - 2, 0, -1):
            suff[i][j] = max(suff[i][j], suff[i][j + 1])
    freq = Counter()
    ans = tot
    for i in a:
        if i == c:
            continue
        freq[i] += 1
        ans = max(ans, suff[i][freq[i]] - nums[i][freq[i]] + 1 + tot)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)