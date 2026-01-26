import itertools

def main(n):
    # n 作为题目数量
    if n < 2:
        print(0)
        return

    # 确定性生成参数
    l = n
    r = n * (n + 1) // 2
    x = max(1, n // 3)

    # 确定性生成题目难度数组 problems，长度为 n
    problems = [i + 1 for i in range(n)]

    result = 0
    for i in range(2, n + 1):
        for comb in itertools.combinations(problems, i):
            summ = sum(comb)
            mini = min(comb)
            maxx = max(comb)
            if l <= summ <= r and maxx - mini >= x:
                result += 1
    print(result)

if __name__ == "__main__":
    main(10)