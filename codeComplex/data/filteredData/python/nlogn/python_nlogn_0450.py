import random

def main(n: int):
    # 生成测试数据：
    # 1. n 是数组长度
    # 2. 随机生成一个数组 nums，元素范围 [1, n]
    # 3. 随机选择一个 nums 中的元素作为 m
    if n <= 0:
        return

    nums = [random.randint(1, n) for _ in range(n)]
    m = random.choice(nums)

    left = {}
    right = {}

    leftl = 0
    leftm = 0

    rightl = 0
    rightm = 0

    start = nums.index(m)

    ans = 1

    # left side
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

    # right side
    for i in range(start + 1, n):
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

    for i in left.keys():
        poss = -i
        if poss in right:
            ans += right[poss] * left[i]

        if poss + 1 in right:
            ans += right[poss + 1] * left[i]

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)