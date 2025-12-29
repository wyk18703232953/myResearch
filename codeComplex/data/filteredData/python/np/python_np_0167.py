from itertools import combinations
import random

def main(n: int) -> int:
    """
    n 作为规模参数：
    - 题目数量 num = n
    - 难度数组 arr 随机生成，长度为 num
    - 其他参数按 num 自适应生成：
        min_dif, max_dif: 难度和的区间
        easy_hard_dif   : 最小难度差
    返回：满足条件的组合数量
    """

    # 规模设定
    num = n

    # 难度数据生成（可按需修改策略）
    random.seed(0)
    arr = [random.randint(1, 100) for _ in range(num)]

    # 生成参数（示例策略：基于 arr 的统计数据）
    total_sum = sum(arr)
    min_dif = total_sum // 3          # 难度和下界
    max_dif = (total_sum * 2) // 3    # 难度和上界
    easy_hard_dif = max(1, max(arr) // 4)  # 最小难度差

    all_combinations = []
    for x in range(2, num + 1):
        for abc in combinations(arr, x):
            all_combinations.append(list(abc))

    possible_answers = 0
    for a in all_combinations:
        s = sum(a)
        if min_dif <= s <= max_dif and max(a) - min(a) >= easy_hard_dif:
            possible_answers += 1

    print(possible_answers)
    return possible_answers


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)