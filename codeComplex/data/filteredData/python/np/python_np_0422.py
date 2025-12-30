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
        if bit_tmp == ans[0]:
            idx_i = i
        if bit_tmp == ans[1]:
            idx_j = i
    return idx_i + 1, idx_j + 1


def main(n):
    # 生成测试数据：
    # 设定 m，使得 2^m 不至于太大，这里简单取 m = min(8, max(1, n))
    m = max(1, min(8, n))

    # data 为 n 行 m 列的矩阵，元素在 [0, 10^9+7] 之间
    MAX_VAL = 10**9 + 7
    random.seed(0)
    data = [[random.randint(0, MAX_VAL) for _ in range(m)] for _ in range(n)]

    a, b = 0, MAX_VAL
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

    idx1, idx2 = backtracking(candidate, ans, data)
    # 按原程序的输出格式
    print(f"{idx1} {idx2}")


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)