import random

def main(n):
    # 生成测试数据：
    # 1. 随机生成目标值 c
    # 2. 随机生成长度为 n 的数组 nums，元素在 [1, n] 范围内
    if n <= 0:
        return

    c = random.randint(1, n)
    nums = [random.randint(1, n) for _ in range(n)]

    # ===== 原逻辑开始（去掉 input() 部分） =====
    # c is the target number
    # number of c values seen
    cPast = 0  # 未被使用，但保留以忠实原代码结构
    countC = 0

    for value in nums:
        if value == c:
            countC += 1

    def sawC(groupsList):
        for key, groups in groupsList.items():
            if groups[-1] < 0:
                groups[-1] -= 1
            else:
                groups += [-1]
        return groupsList

    solution = countC
    # other numbers, highest count stored in hash table
    groupsList = {}
    for num in nums:
        if num == c:
            groupsList = sawC(groupsList)
        elif num in groupsList.keys():
            if groupsList[num][-1] > 0:
                groupsList[num][-1] += 1
            else:
                groupsList[num] += [1]
        else:
            groupsList[num] = [1]

    for key, groups in groupsList.items():
        # actually counting if good
        maxDiff = 1
        currDiff = 0
        for group in groups:
            currDiff += group
            if group > currDiff:
                currDiff = group
            if currDiff > maxDiff:
                maxDiff = currDiff
        if maxDiff + countC > solution:
            solution = countC + maxDiff

    print(solution)


# 示例调用
if __name__ == "__main__":
    main(10)