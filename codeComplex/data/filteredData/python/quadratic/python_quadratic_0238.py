from math import inf
import random


def main(n: int):
    # 生成测试数据：随机生成 s_list 和 c_list
    # s_list：1~1000 的随机整数
    # c_list：1~1000 的随机整数
    random.seed(0)
    s_list = [random.randint(1, 1000) for _ in range(n)]
    c_list = [random.randint(1, 1000) for _ in range(n)]

    total_min = inf
    for j in range(n):
        min_i = inf
        for i in range(0, j):
            if s_list[i] < s_list[j]:
                min_i = min(min_i, c_list[i])

        min_k = inf
        for k in range(j + 1, n):
            if s_list[k] > s_list[j]:
                min_k = min(min_k, c_list[k])

        total_min = min(total_min, min_i + c_list[j] + min_k)

    if total_min != inf:
        print(total_min)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)