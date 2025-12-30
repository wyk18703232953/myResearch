import random

def main(n):
    # 根据 n 生成测试数据：长度固定为 14，每个位置为 0~n 的随机整数
    # 如需其他生成规则，可在此处修改
    grid = [random.randint(0, n) for _ in range(14)]

    max_res = 0
    for i in range(14):
        g_c = grid.copy()
        Amount = g_c[i] // 14
        Amount_r = g_c[i] % 14

        if Amount > 0:
            for j in range(14):
                idx = (i + j + 1) % 14
                if i != idx:
                    g_c[idx] += Amount
                    g_c[i] -= Amount

        if Amount_r > 0:
            for j in range(14):
                if Amount_r <= 0:
                    break
                idx = (i + j + 1) % 14
                if i != idx:
                    g_c[idx] += 1
                    Amount_r -= 1
                    g_c[i] -= 1

        res = 0
        for k in range(14):
            if g_c[k] % 2 == 0:
                res += g_c[k]

        max_res = max(max_res, res)

    print(max_res)


if __name__ == "__main__":
    # 示例：n = 100
    main(100)