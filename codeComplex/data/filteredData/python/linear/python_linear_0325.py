def main(n):
    # n 表示每组字符串的规模，t = n
    t = max(1, n)

    # 确定性生成 last 和 current
    # last: ["s0", "s1", ..., "s(t-1)"]
    last = ["s{}".format(i) for i in range(t)]
    # current: ["s0", "s1", ..., "s(t-1)"] 的一个确定性扰动版本
    # 规则：偶数下标保持，奇数下标改为 "x{i}"
    current = ["s{}".format(i) if i % 2 == 0 else "x{}".format(i) for i in range(t)]

    # 以下为原逻辑的非交互版本
    last_copy = [str(x) for x in last]
    current_copy = [str(x) for x in current]

    for i in range(t):
        if last_copy[i] in current_copy:
            idx = current_copy.index(last_copy[i])
            current_copy[idx] = "*"
            last_copy[i] = "*"

    last_copy.sort()
    current_copy.sort()

    total = 0
    for i in range(t):
        if last_copy[i] == current_copy[i]:
            continue

        else:
            total += 1

    # print(total)
    pass
if __name__ == "__main__":
    main(10)