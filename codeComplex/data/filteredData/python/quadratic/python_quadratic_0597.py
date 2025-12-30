import math
import random


def main(n: int):
    # 生成测试数据
    # 这里根据 n 随机生成 m、k 和数组 arr
    # 可按需要调整数据规模和范围
    m = random.randint(1, max(1, n))       # 1 <= m <= n
    k = random.randint(-10, 10)            # k 在 [-10, 10] 内
    arr = [random.randint(-10, 10) for _ in range(n)]

    # 原程序逻辑开始
    part_sum = [0]
    for i in range(n):
        part_sum.append(part_sum[-1] + arr[i])

    part_sum_add = [[] for _ in range(m)]
    min_in_part_sum_add = [[] for _ in range(m)]

    for shift in range(m):
        count_blocks = math.ceil((n - shift) / m + 1)
        prev_min_in_part_sum_add = None
        for i in range(n + 1):
            cur_part_sum = part_sum[i] + k * (count_blocks - ((i - shift) // m))
            if i == 0 or cur_part_sum < prev_min_in_part_sum_add:
                cur_min_in_part_sum_add = cur_part_sum
            else:
                cur_min_in_part_sum_add = prev_min_in_part_sum_add

            part_sum_add[shift].append(cur_part_sum)
            min_in_part_sum_add[shift].append(cur_min_in_part_sum_add)
            prev_min_in_part_sum_add = cur_min_in_part_sum_add

    max_result = 0
    for i in range(1, n + 1):
        current_shift = i % m
        current_min = min_in_part_sum_add[current_shift][i]
        current_ans = part_sum_add[current_shift][i] - current_min
        if current_ans > max_result:
            max_result = current_ans

    # 输出结果
    print(max_result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)