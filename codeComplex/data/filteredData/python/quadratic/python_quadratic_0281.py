def main(n):
    # 映射：n -> 序列长度 n，指纹长度 m = max(1, n // 2)
    m = max(1, n // 2)

    # 生成确定性的 sequence（字符串列表）
    sequence = [str(i) for i in range(n)]

    # 生成确定性的 fingerprint
    # 前半部分与 sequence 有交集，后半部分为与 sequence 不重叠的元素
    overlap_len = min(m, n)
    fingerprint = [str(i) for i in range(overlap_len)]
    if m > overlap_len:
        fingerprint += [str(n + i) for i in range(m - overlap_len)]

    # 保持原始算法逻辑：过滤出 sequence 中出现在 fingerprint 中的元素
    result = " ".join(i for i in sequence if i in fingerprint)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)