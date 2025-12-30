import random

def solve(n, arr):
    s = sum(arr)
    if s == 0:
        return "cslnb"

    n_num = {}

    for item in arr:
        if item in n_num:
            n_num[item] += 1
        else:
            n_num[item] = 1

    if 0 in n_num and n_num[0] >= 2:
        return 'cslnb'

    for key in n_num.keys():
        if n_num[key] >= 3:
            return "cslnb"

    ind_pairs = []
    for key in n_num.keys():
        if n_num[key] == 2:
            ind_pairs.append(key)

    if len(ind_pairs) >= 2:
        return "cslnb"
    elif len(ind_pairs) == 1 and (ind_pairs[0] - 1) in n_num:
        return "cslnb"
    else:
        sum_targ = n * (n - 1) // 2
        dif_sum = s - sum_targ
        if dif_sum % 2 == 0:
            return "cslnb"
        else:
            return "sjfnb"


def main(n):
    # 生成规模为 n 的测试数据
    # 生成非负整数数组，范围可根据需要调整
    max_val = max(0, 2 * n)
    arr = [random.randint(0, max_val) for _ in range(n)]

    # 输出结果
    print(solve(n, arr))


if __name__ == "__main__":
    # 示例：固定一个 n 运行
    main(5)