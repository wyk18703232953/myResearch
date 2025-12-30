import random

def main(n):
    # 1. 生成测试数据
    # 保证 E 严格递增，以符合原题常见场景（如 Codeforces 题中要求）
    # U 选为一个与 E 范围同量级的整数
    if n < 3:
        # 原逻辑中 n<3 时外层 for 不会进入，直接输出 -1
        print(-1)
        return

    # 生成递增数组 E
    E = []
    cur = 0
    for _ in range(n):
        cur += random.randint(1, 10)  # 每次递增 1~10
        E.append(cur)

    # 生成 U，使得有一定概率存在 (Ek - Ei) <= U 的三元组
    total_span = E[-1] - E[0]
    if total_span <= 0:
        U = 0
    else:
        # 在 1 ~ 总跨度 之间随机
        U = random.randint(1, total_span)

    # 2. 将原始逻辑封装，无 input()
    prev_ind_k = 2
    maxi_efficiency = -1.0

    for ind_i in range(0, n - 2):
        ind_j = ind_i + 1
        prev_ind_k = max(prev_ind_k, ind_i + 2)
        Ei = E[ind_i]
        Ej = E[ind_j]
        for ind_k in range(prev_ind_k, n + 1):
            if ind_k == n:
                prev_ind_k = n - 1
                break
            Ek = E[ind_k]
            if (Ek - Ei) > U:
                prev_ind_k = ind_k - 1
                break

            efficiency = (Ek - Ej) / (Ek - Ei)
            if efficiency > maxi_efficiency:
                maxi_efficiency = efficiency

    # 3. 输出结果（以及可选地输出生成的数据便于调试）
    print("n =", n)
    print("U =", U)
    print("E =", E)
    print("max_efficiency =", maxi_efficiency)


if __name__ == "__main__":
    # 示例：调用 main，n 可按需修改
    main(10)