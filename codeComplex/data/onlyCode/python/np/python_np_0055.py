actual = input()
processed = input()


def factorial(num: int):
    res = 1
    while num >= 1:
        res *= num
        num -= 1
    return res


actualPos = actual.count('+')
actualNeg = actual.count('-')
processedPos = processed.count('+')
processedNeg = processed.count('-')

if processedPos > actualPos or processedNeg > actualNeg:
    print(0)
elif processedPos == actualPos and processedNeg == actualNeg:
    print(1)
else:
    remainPos = actualPos - processedPos
    remainNeg = actualNeg - processedNeg

    print((factorial(remainPos + remainNeg) / (factorial(remainPos) * factorial(remainNeg))) / 2 ** (
            remainPos + remainNeg))
