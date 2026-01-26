def main(n):
    # 映射规则：
    # n >= 2 时：序列长度 = n，指纹长度 = n // 2
    # n == 1 时：退化为最小可运行规模：序列长度 = 1，指纹长度 = 1
    # n <= 0 时：返回空结果
    if n <= 0:
        # print("")
        pass
        return
    if n == 1:
        seq_len = 1
        fp_len = 1

    else:
        seq_len = n
        fp_len = max(1, n // 2)

    # 构造与原始程序一致的“输入结构”：
    # 第一行: n m
    # 第二行: sequence（长度为 seq_len）
    # 第三行: fingerprint（长度为 fp_len）
    # 元素为确定性的字符串形式的整数

    # sequence: 0, 1, 2, ..., seq_len-1
    sequence = [str(i) for i in range(seq_len)]

    # fingerprint: 从 0 开始，每隔 2 取一个元素
    # 例如 seq_len=5, fp_len=2 -> fingerprint = ["0", "2"]
    fingerprint = [str((2 * i) % seq_len) for i in range(fp_len)]

    # 保持原算法逻辑：筛选 sequence 中出现在 fingerprint 的元素
    result = " ".join(i for i in sequence if i in fingerprint)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 来进行规模实验
    main(10)