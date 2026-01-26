import math

def main(n):
    # n 表示天数
    all_days_problems = [(i % 7) + 1 for i in range(1, n + 1)]
    sum_count = sum(all_days_problems)
    half_problems = math.ceil(sum_count / 2)
    current_sum = 0
    answer = 0
    for num in all_days_problems:
        answer += 1
        current_sum += num
        if current_sum >= half_problems:
            break
    # print(answer)
    pass
if __name__ == "__main__":
    main(10)