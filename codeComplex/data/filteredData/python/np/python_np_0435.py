import random

def main(n):
    # 这里令 n = N，列数 M 可自行设定，比如固定为 5
    N = n
    M = 5

    # 3. 根据 n 生成测试数据：生成一个 N x M 的随机整数矩阵 state
    # 数值范围可根据需要调整，这里设为 0 ~ 10^9
    MAX_VAL = 10**9
    random.seed(0)
    state = [[random.randint(0, MAX_VAL) for _ in range(M)] for _ in range(N)]

    Ans = {}

    l = -1
    r = 10**9 + 1
    while r - l > 1:
        m = (l + r) // 2
        T = {}
        for j, S in enumerate(state):
            bit = 0
            for i, s in enumerate(S):
                if s >= m:
                    bit += 1 << i
            T[bit] = j

        ok = False
        full_mask = (1 << M) - 1
        for bit1 in range(1 << M):
            if ok:
                break
            if bit1 not in T:
                continue
            for bit2 in range(1 << M):
                if (bit1 | bit2) == full_mask and bit2 in T:
                    ok = True
                    Ans[m] = [T[bit1], T[bit2]]
                    break

        if ok:
            l = m
        else:
            r = m

    # 如果 l 仍为 -1，说明没有找到任何可行解，此时避免访问 Ans[-1]
    if l in Ans:
        i1, i2 = Ans[l][0] + 1, Ans[l][1] + 1
    else:
        # 兜底策略：随便输出两个下标（若 N >= 2）
        i1, i2 = 1, min(2, N)

    print(i1, i2)


if __name__ == "__main__":
    # 示例：调用 main(10)，对应 N=10
    main(10)