import random

def find_pair(candidate, data, m):
    ans = (-1, -1)
    binary_bit = [False for _ in range(1 << m)]
    for row in data:
        bit_tmp = 0
        for j in range(len(row)):
            if row[j] >= candidate:
                bit_tmp |= 1 << j
        binary_bit[bit_tmp] = True

    full_mask = (1 << m) - 1
    for i in range(1 << m):
        if not binary_bit[i]:
            continue
        for j in range(1 << m):
            if binary_bit[j] and (i | j) == full_mask:
                ans = (i, j)
                return ans
    return ans

def backtracking(candidate, ans, data):
    idx_i = -1
    idx_j = -1
    for i in range(len(data)):
        bit_tmp = 0
        for j in range(len(data[i])):
            if data[i][j] >= candidate:
                bit_tmp |= 1 << j
        if bit_tmp == ans[0] and idx_i == -1:
            idx_i = i
        if bit_tmp == ans[1] and idx_j == -1:
            idx_j = i
    print(str(idx_i + 1) + " " + str(idx_j + 1))

def main(n):
    # 规模参数：n 为行数，列数 m 由 n 推导或固定设定
    # 这里设定 m = min(8, n) 保证复杂度可控（因有 2^m 状态）
    m = min(8, max(1, n))

    # 根据 n, m 生成测试数据
    # 生成范围控制在 [0, 10^9+7] 内，保持与原代码一致的量级
    MOD = 10**9 + 7
    random.seed(0)
    data = [[random.randint(0, MOD) for _ in range(m)] for _ in range(n)]

    a = 0
    b = MOD
    ans = (-1, -1)
    candidate = -1

    while a <= b:
        mid = (a + b) // 2
        bin_ans = find_pair(mid, data, m)
        if bin_ans[0] != -1 and bin_ans[1] != -1:
            ans = bin_ans
            candidate = mid
            a = mid + 1
        else:
            b = mid - 1

    backtracking(candidate, ans, data)

if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)