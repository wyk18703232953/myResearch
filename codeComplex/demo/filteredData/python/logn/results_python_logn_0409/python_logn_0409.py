def solve(n, k):
    from math import ceil
    if k == 1:
        return n - 1
    if k == 2:
        if n > 1:
            return n - 1

        else:
            return -1
    if k == 3:
        if n > 2:
            return n - 1

        else:
            return -1
    if k in {4, 5}:
        if n > 1:
            return n - 2

        else:
            return -1

    if 2 * n + 1 <= len(bin(3 * k)[2:]):
        return -1

    else:
        return n - ceil((len(bin(3 * k)[2:]) - 1) / 2)


def main(n):
    # n 作为测试组数规模
    t = n
    outputs = []
    for i in range(t):
        # 确定性生成 n_i, k_i
        ni = i + 2              # 保证从 2 开始递增
        ki = (i % 7) + 1        # 在 1~7 之间循环，覆盖各分支
        a = solve(ni, ki)
        if a == -1:
            outputs.append("NO")

        else:
            outputs.append(f"YES {a}")
    for line in outputs:
        # print(line)
        pass
if __name__ == "__main__":
    main(10)