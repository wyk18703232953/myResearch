def GSB(x):
    counter = 0
    while x != 0:
        counter += 1
        x = x >> 1
    return counter


def main(n):
    # 映射规则：
    # problems = n
    # minimum = n
    # maximum = 2 * n
    # difference = n // 2
    # array 长度 = problems，内容为 1..problems 的平方
    problems = max(1, n)
    minimum = n
    maximum = 2 * n
    difference = n // 2

    array = [(i + 1) * (i + 1) for i in range(problems)]

    combinations = [int(x) for x in range(2 ** problems)]
    total = 0

    for i in combinations:
        checker = [x for x in array] + ["a"]
        j = 0
        z = GSB(i)
        check = 1
        while j != z and i != 0:
            if i & 1 == 1:
                checker[j] = "a"
                check += 1
            i = i >> 1
            j += 1
        for _ in range(check):
            checker.remove("a")
        checker.sort()
        if (
            minimum <= sum(checker) <= maximum
            and len(checker) >= 2
            and checker[-1] - checker[0] >= difference
        ):
            total += 1

    print(total)


if __name__ == "__main__":
    main(5)