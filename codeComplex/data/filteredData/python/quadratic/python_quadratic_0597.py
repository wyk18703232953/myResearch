import math

def main(n):
    # 映射规模：n 为数组长度，m 和 k 由 n 确定性生成
    if n <= 0:
        return 0

    m = max(1, n // 3)
    k = n // 2

    # 确定性生成数组 arr，长度为 n
    # 使用简单算术构造：arr[i] = (i * 3 + 1) % (n + 5)
    arr = [(i * 3 + 1) % (n + 5) for i in range(n)]

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
            if i == 0 or prev_min_in_part_sum_add is None or cur_part_sum < prev_min_in_part_sum_add:
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

    print(max_result)
    return max_result

if __name__ == "__main__":
    # 示例调用：规模为 10
    main(10)