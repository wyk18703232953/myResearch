import sys

def generate_nm(n):
    if n <= 0:
        return 1, 1
    # 确定性映射：让 n 同时控制行列规模
    # 保证至少为 1
    rows = n
    cols = n + (n // 2)
    if cols <= 0:
        cols = 1
    return rows, cols

def main(n):
    n_rows, m_cols = generate_nm(n)
    n, m = n_rows, m_cols

    if m % 2 == 0:
        steps = []
        for j in range(m // 2):
            for i in range(n):
                steps.append((j, i))
                steps.append((m - j - 1, n - i - 1))

    else:
        steps = []
        for j in range(m // 2):
            for i in range(n):
                steps.append((j, i))
                steps.append((m - j - 1, n - i - 1))
        l = 0
        r = n - 1
        mid = m // 2
        while l <= r:
            steps.append((mid, l))
            if l != r:
                steps.append((mid, r))
            l += 1
            r -= 1

    out_lines = []
    for x, y in steps:
        out_lines.append(f"{y+1} {x+1}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    # 示例：使用一个固定的 n 调用，便于实验时修改
    main(5)