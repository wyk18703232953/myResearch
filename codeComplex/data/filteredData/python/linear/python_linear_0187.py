import math
import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据：n 天每天的题目数量
    #    这里假设每一天做题数量在 [0, 10] 内，可按需要修改
    all_days_problems = [random.randint(0, 10) for _ in range(n)]

    # 2. 原逻辑：找到最少的天数，使得前缀和 >= 总题目数的一半（向上取整）
    sum_count = sum(all_days_problems)
    half_problems = math.ceil(sum_count / 2)

    current_sum = 0
    answer = 0
    for num in all_days_problems:
        answer += 1
        current_sum += num
        if current_sum >= half_problems:
            break

    # 输出结果（可视需要也输出测试数据以便检查）
    print(answer)

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)