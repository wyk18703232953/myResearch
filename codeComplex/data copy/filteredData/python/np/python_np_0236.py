def isValidSet(problemSet: list, minTotalDif: int, maxTotalDif: int, minDelta: int) -> bool:
    if len(problemSet) >= 2:
        total = sum(problemSet)
        myDelta = max(problemSet) - min(problemSet)
        if minTotalDif <= total <= maxTotalDif and myDelta >= minDelta:
            return True
    return False

def countValidSubsets(problems: list, minTotalDif: int, maxTotalDif: int, minDelta: int) -> int:
    def subsetBuilder(problems: list, currentSubset: list, nextElementIndex: int) -> None:
        if isValidSet(currentSubset, minTotalDif, maxTotalDif, minDelta):
            validSubsets.append(list(currentSubset))
        for i in range(nextElementIndex, len(problems)):
            currentSubset.append(problems[i])
            subsetBuilder(problems, currentSubset, i + 1)
            currentSubset.pop()

    index = 0
    currentSubset = []
    validSubsets = []
    subsetBuilder(problems, currentSubset, index)
    return len(validSubsets)

def main(n: int) -> int:
    if n <= 0:
        return 0
    probs = [i % 10 + 1 for i in range(1, n + 1)]
    l = n
    r = 2 * n
    x = max(1, n // 4)
    return countValidSubsets(probs, l, r, x)

if __name__ == "__main__":
    result = main(10)
    print(result)