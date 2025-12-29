import random

MAXV = 500000

def solve(n, c, a):
    nums = [[0] for _ in range(MAXV + 1)]
    freq = [0] * (MAXV + 1)
    minus = 0

    for x in a:
        if x == c:
            minus += 1
        else:
            freq[x] += 1
            nums[x].append(freq[x] - minus)

    tot = minus
    suff = [row[:] for row in nums]

    for i in range(MAXV + 1):
        # from len(nums[i]) - 2 down to 1
        for j in range(len(nums[i]) - 2, 0, -1):
            suff[i][j] = max(suff[i][j], suff[i][j + 1])

    freq = [0] * (MAXV + 1)
    ans = tot

    for x in a:
        if x == c:
            continue
        freq[x] += 1
        ans = max(ans, suff[x][freq[x]] - nums[x][freq[x]] + 1 + tot)

    return ans


def main(n: int):
    # 生成测试数据：
    # n 个元素的数组 a，元素取值范围 [1, MAXV]，c 为其中一个随机值
    if n <= 0:
        return None

    a = [random.randint(1, MAXV) for _ in range(n)]
    c = random.choice(a)

    result = solve(n, c, a)
    print(result)


if __name__ == "__main__":
    # 示例：可在此修改 n 以测试不同规模
    main(10)