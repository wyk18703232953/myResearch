import sys

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
    m = len(data[0]) if data else 0
    for i in range(len(data)):
        bit_tmp = 0
        for j in range(m):
            if data[i][j] >= candidate:
                bit_tmp |= 1 << j
        if bit_tmp == ans[0]:
            idx_i = i
        if bit_tmp == ans[1]:
            idx_j = i
    print(str(idx_i + 1) + " " + str(idx_j + 1))

def generate_data(n):
    # Map n to a deterministic (n, m) and data:
    # Let number of rows be n, number of columns be m = min(20, max(1, n % 10 + 1))
    m = n % 10 + 1
    if m > 20:
        m = 20
    data = []
    for i in range(n):
        row = []
        base = i + 1
        for j in range(m):
            # Deterministic integer construction, grows with n, i, j
            val = base * (j + 1) + (i // 2) + j * j
            row.append(val)
        data.append(row)
    return n, m, data

def main(n):
    if n <= 0:
        return
    n_rows, m, data = generate_data(n)
    a = 0
    b = 10 ** 9 + 7
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
    # Example deterministic call; adjust n as needed for experiments
    main(10)