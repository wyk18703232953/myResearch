def main(n):
    # 生成确定性输入：n 表示约会数量，缓冲时间 s 与时间点序列都由 n 推导
    # 这里约定：
    # - s = n，即缓冲时间随规模线性增长
    # - 共有 n 个约会时间点，第 i 个约会时间为 (i * 3) 分钟
    # 这样时间点严格递增且完全确定
    s = n
    l = [0]
    for i in range(n):
        q = (i + 1) * 3  # 第 i+1 个约会时间（单位：分钟）
        l.append(q)
    if l[1] - l[0] > s:
        # print(0, 0)
        pass
        return
    for i in range(n):
        if l[i + 1] - l[i] > 2 * s + 1:
            l[i] += s + 1
            # print(l[i] // 60, l[i] % 60)
            pass
            return
    l[-1] += s + 1
    # print(l[-1] // 60, l[-1] % 60)
    pass
if __name__ == "__main__":
    # 示例：使用 n=10 作为规模
    main(10)