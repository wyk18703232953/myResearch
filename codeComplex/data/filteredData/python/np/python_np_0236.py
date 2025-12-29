import random

def isValidSet(problemSet: list, minTotalDif: int, maxTotalDif: int, minDelta: int) -> bool:
    if len(problemSet) >= 2:
        total = sum(problemSet)
        myDelta = max(problemSet) - min(problemSet)
        if minTotalDif <= total <= maxTotalDif and myDelta >= minDelta:
            return True
    return False


def countValidSubsets(problems: list, minTotalDif: int, maxTotalDif: int, minDelta: int) -> int:
    validSubsets = []

    def subsetBuilder(problems: list, currentSubset: list, nextElementIndex: int) -> None:
        if isValidSet(currentSubset, minTotalDif, maxTotalDif, minDelta):
            validSubsets.append(list(currentSubset))
        for i in range(nextElementIndex, len(problems)):
            currentSubset.append(problems[i])
            subsetBuilder(problems, currentSubset, i + 1)
            currentSubset.pop()

    subsetBuilder(problems, [], 0)
    return len(validSubsets)


def main(n: int) -> None:
    # 生成测试数据：
    # n: 题目数量
    # 难度值在 1~1000 之间
    # l, r: 随机生成可行范围，使得存在一些子集满足条件的概率较大
    probs = [random.randint(1, 1000) for _ in range(n)]
    total_sum = sum(probs)

    # 生成一个相对合理的 (l, r, x)
    l = random.randint(1, max(1, total_sum // 2))
    r = random.randint(l, total_sum)
    x = random.randint(0, max(0, max(probs) - min(probs)))

    ans = countValidSubsets(probs, l, r, x)
    print(ans)


if __name__ == "__main__":
    # 示例：规模 n=10
    main(10)