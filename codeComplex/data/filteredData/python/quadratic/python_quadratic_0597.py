import math

def main(n):
    # 映射输入结构：
    # 原程序输入：n, m, k 和 n 个数组元素
    # 这里将参数 n 视为数组长度
    # 构造：
    #   m = max(1, n // 3)  保证与 n 同阶，又不为 0
    #   k = n              线性规模，保证非 0
    #   arr: 长度为 n 的确定性整数数组
    #        使用简单算术构造：arr[i] = (i * 2 - i // 3)
    if n <= 0:
        return 0

    m = max(1, n // 3)
    k = n
    arr = [(i * 2 - i // 3) for i in range(n)]

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

    # print(max_result)
    pass
    return max_result

if __name__ == "__main__":
    # 示例规模，可根据需要修改
    main(10)