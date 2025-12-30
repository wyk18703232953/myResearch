import itertools
import random

def main(n):
    # 生成测试数据
    # 为了构造有意义的数据，设定：
    #   问题难度在 [1, 100] 范围内
    #   下界 l, 上界 r, 以及 x 也随机生成
    random.seed(0)  # 固定种子，便于复现
    problems = [random.randint(1, 100) for _ in range(n)]

    # 生成 l, r, x
    total_sum = sum(problems)
    l = random.randint(0, total_sum // 2 if total_sum > 1 else 0)
    r = random.randint(l, total_sum)  # 确保 l <= r
    x = random.randint(0, 50)

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
    # 示例：调用 main，规模 n 可按需修改
    main(5)