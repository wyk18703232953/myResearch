import random

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

def probToMove(dist, questionMarks):
    if dist > questionMarks:
        return 0.0
    reducedDist = questionMarks - dist
    if reducedDist % 2 != 0:
        return 0.0
    dist = reducedDist // 2 + dist
    headsOrders = factorial(questionMarks) / (factorial(dist) * factorial(questionMarks - dist))
    totalPossibilities = 2 ** questionMarks
    return headsOrders / totalPossibilities

def main(n):
    # 生成测试数据：
    # line1: 长度为 n，仅包含 '+' 和 '-'
    # line2: 长度为 n，包含 '+', '-', '?' 的随机组合
    choices_line1 = ['+', '-']
    choices_line2 = ['+', '-', '?']

    line1 = ''.join(random.choice(choices_line1) for _ in range(n))
    line2 = ''.join(random.choice(choices_line2) for _ in range(n))

    truePosition = 0
    fakePosition = 0
    questionMarks = 0

    for i in range(n):
        if line1[i] == '+':
            truePosition += 1
        if line1[i] == '-':
            truePosition -= 1
        if line2[i] == '+':
            fakePosition += 1
        if line2[i] == '-':
            fakePosition -= 1
        if line2[i] == '?':
            questionMarks += 1

    distanceToMove = abs(truePosition - fakePosition)
    result = probToMove(distanceToMove, questionMarks)
    print(result)


# 示例：当作为脚本运行时，可以调用 main(10)
if __name__ == "__main__":
    main(10)