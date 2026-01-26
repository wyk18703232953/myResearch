import sys


def generate_input_from_n(n):
    # 映射规则：n 作为原程序的 n，k = max(1, n // 2)
    # 这样整体规模大约为 O(n^2)
    if n < 1:
        n = 1
    k = max(1, n // 2)
    return n, k


def core_algorithm(n, k):
    ans = []
    total = n * k
    for i in range(1, total + 1):
        if i % 2:
            x, y = divmod(i // 2, k)
            ans.append([x + 1, y + 1])

        else:
            x, y = divmod(total - i // 2, k)
            ans.append([x + 1, y + 1])
    return ans


def main(n):
    n_val, k_val = generate_input_from_n(n)
    result = core_algorithm(n_val, k_val)
    out_lines = []
    for pair in result:
        out_lines.append(f"{pair[0]} {pair[1]}")
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    # 示例：使用 n = 10 作为输入规模
    main(10)