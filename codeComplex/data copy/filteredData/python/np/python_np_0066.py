def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


def probToMove(dist, questionMarks):
    if dist > questionMarks:
        return float(0)
    reducedDist = questionMarks - dist
    if reducedDist % 2 != 0:
        return float(0)
    dist = reducedDist // 2 + dist
    headsFlips = 1
    headsOrders = factorial(questionMarks) / (factorial(dist) * factorial(questionMarks - dist))
    totalPossibilities = 2 ** questionMarks
    return headsFlips * headsOrders / totalPossibilities


def main(n):
    if n <= 0:
        n = 1
    # 构造 line1，使其最终位置为 0，长度为 n
    # 前一半是 '+', 后一半是 '-'（若 n 为奇数，多一个 '+'）
    half = n // 2
    if n % 2 == 0:
        line1 = "+" * half + "-" * half
    else:
        line1 = "+" * (half + 1) + "-" * half

    # 构造 line2，前 half 个为确定符号，后半部分为 '?'
    # 确定符号使得假位置与真位置有一定偏差，偏差随 n 线性增长但完全确定
    deterministic_shift = n // 3
    fixed_part = []
    for i in range(half):
        if i < deterministic_shift:
            fixed_part.append("+")
        else:
            fixed_part.append("-")
    fixed_part = "".join(fixed_part)
    question_part = "?" * (n - len(fixed_part))
    line2 = fixed_part + question_part

    truePosition = 0
    fakePosition = 0
    questionMarks = 0
    for i in range(len(line1)):
        if line1[i] == "+":
            truePosition += 1
        if line1[i] == "-":
            truePosition -= 1
        if line2[i] == "+":
            fakePosition += 1
        if line2[i] == "-":
            fakePosition -= 1
        if line2[i] == "?":
            questionMarks += 1

    distanceToMove = abs(truePosition - fakePosition)

    result = probToMove(distanceToMove, questionMarks)
    print(result)


if __name__ == "__main__":
    main(10)