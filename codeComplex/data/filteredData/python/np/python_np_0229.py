import random

def GSB(x):
    counter = 0
    while x != 0:
        counter += 1
        x = x >> 1
    return counter

def main(n):
    # 生成测试数据
    # n 作为 problems 的规模，其它参数和数组按 n 生成
    problems = n
    # 为了让数据合理一些，生成 array 中的值在 1~100 之间
    array = [random.randint(1, 100) for _ in range(problems)]
    total_sum = sum(array)
    # 生成 minimum, maximum, difference
    # minimum 和 maximum 在 [0, total_sum] 范围内，确保 minimum <= maximum
    minimum = random.randint(0, total_sum // 2)
    maximum = random.randint(minimum, total_sum)
    # difference 在 [0, max(array) - min(array)] 范围内
    if problems > 0:
        diff_max = max(array) - min(array)
        difference = random.randint(0, diff_max)
    else:
        difference = 0

    combinations = [int(x) for x in range(2 ** problems)]
    total = 0

    for i in combinations:
        checker = [x for x in array] + ['a']
        j = 0
        z = GSB(i)
        check = 1
        tmp = i
        while j != z and tmp != 0:
            if tmp & 1 == 1:
                checker[j] = 'a'
                check += 1
            tmp = tmp >> 1
            j += 1
        for _ in range(check):
            checker.remove('a')
        checker.sort()
        if (
            len(checker) >= 2
            and minimum <= sum(checker) <= maximum
            and checker[-1] - checker[0] >= difference
        ):
            total += 1
    print(total)

if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)