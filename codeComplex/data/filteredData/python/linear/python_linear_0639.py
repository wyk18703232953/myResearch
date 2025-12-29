import random

def main(n):
    # 生成测试数据：长度为 n 的最大度数数组
    # 这里示例：每个最大度数在 [0, n-1] 之间随机生成
    random.seed(0)
    max_degs = [random.randint(0, n - 1) for _ in range(n)]

    B = [[i + 1, x] for i, x in enumerate(max_degs) if x >= 2]
    S = [[i + 1, x] for i, x in enumerate(max_degs) if x < 2]

    if 2 + sum(b - 2 for _, b in B) < len(S):
        print('NO')
        return

    print('YES', len(B) + min(len(S), 2) - 1)
    print(n - 1)

    # B edges
    for k in range(len(B) - 1):
        i, x = B[k]
        i_n, _ = B[k + 1]
        print(i, i_n)
        B[k][1] -= 1
        B[k + 1][1] -= 1

    k = 0
    for i, (s_idx, _) in enumerate(S):
        if i == 0:
            print(B[0][0], s_idx)
            B[0][1] -= 1
        elif i == 1:
            print(B[-1][0], s_idx)
            B[-1][1] -= 1
        else:
            while B[k][1] == 0:
                k += 1
            print(B[k][0], s_idx)
            B[k][1] -= 1


# 示例调用
if __name__ == "__main__":
    main(5)