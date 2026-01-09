def main(n):
    # n controls the length of nums; c is chosen deterministically
    if n <= 0:
        # print(0)
        pass
        return

    # Deterministic generation of nums and c
    # Example: nums is a repeating pattern of small integers, c is fixed
    c = 3
    nums = [i % 5 for i in range(n)]

    # Original algorithm begins
    cPast = 0
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

    # print(solution)
    pass
if __name__ == "__main__":
    main(10)