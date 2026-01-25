from math import inf


def generate_data(n):
    # 保证 n 至少为 1
    if n <= 0:
        n = 1
    # 生成严格递增的 s_list，方便出现满足条件的三元组
    s_list = [i for i in range(n)]
    # 生成确定性的 c_list，包含一定变化
    c_list = [(i * 3 + 5) % (n + 7) + 1 for i in range(n)]
    return n, s_list, c_list


def core_algorithm(n, s_list, c_list):
    total_min = inf
    for j in range(n):
        min_i = inf
        for i in range(0, j):
            if s_list[i] < s_list[j]:
                if c_list[i] < min_i:
                    min_i = c_list[i]

        min_k = inf
        for k in range(j + 1, n):
            if s_list[k] > s_list[j]:
                if c_list[k] < min_k:
                    min_k = c_list[k]

        cost = min_i + c_list[j] + min_k
        if cost < total_min:
            total_min = cost

    if total_min != inf:
        return total_min
    else:
        return -1


def main(n):
    n, s_list, c_list = generate_data(n)
    result = core_algorithm(n, s_list, c_list)
    print(result)


if __name__ == "__main__":
    main(10)