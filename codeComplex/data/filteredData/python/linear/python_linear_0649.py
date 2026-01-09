def main(n):
    # 将 n 解释为序列长度，c 固定为一个确定性值
    c = n // 2 + 1
    max_val = max(n, c) + 2
    res1 = [0] * (max(500001, max_val))
    res = 0

    # 确定性生成输入序列：长度为 n，元素在 [1, max_val-1] 内
    # 使用简单算术构造
    a_list = [(i * 3 + 1) % (max_val - 1) + 1 for i in range(n)]

    for ai in a_list:
        res1[ai] = max(res1[ai], res1[c])
        res1[ai] += 1
        res = max(res, res1[ai] - res1[c])
    # print(res + res1[c])
    pass
if __name__ == "__main__":
    main(100000)