def main(n):
    # 生成两个长度为 n 的字符串序列，模拟原来的两组输入
    # 使用确定性规则：第一组为 "s{i%k}"，第二组为 "s{(i+1)%k}"
    # 这样可以保证有重复、有差异，且完全由 n 决定
    k = max(1, n // 3 + 1)

    seq1 = [f"s{i % k}" for i in range(n)]
    seq2 = [f"s{(i + 1) % k}" for i in range(n)]

    a_dicts = [{}, {}]
    # 模拟原程序第一组输入
    for x in seq1:
        if x in a_dicts[0]:
            a_dicts[0][x] += 1

        else:
            a_dicts[0][x] = 1
        if x not in a_dicts[1]:
            a_dicts[1][x] = 0

    # 模拟原程序第二组输入
    for x in seq2:
        if x in a_dicts[1]:
            a_dicts[1][x] += 1

        else:
            a_dicts[1][x] = 1
        if x not in a_dicts[0]:
            a_dicts[0][x] = 0

    c = 0
    for k in a_dicts[0]:
        c += abs(a_dicts[0][k] - a_dicts[1][k])
    return c // 2


if __name__ == "__main__":
    # 示例：可以在这里调整 n 进行规模化实验
    n = 10
    # print(main(n))
    pass