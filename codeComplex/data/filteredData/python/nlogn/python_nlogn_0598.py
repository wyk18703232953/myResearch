def main(n):
    from collections import Counter as C

    # 映射含义：
    # n -> 列表长度
    # m -> 取值上界（与 n 同阶，保证可规模化）
    m = max(1, n)  # 防止 n=0
    # 构造确定性列表 l，长度为 n，元素取值在 [1, m] 范围内
    # 使用简单算术生成：周期性分布
    l = [(i % m) + 1 for i in range(n)]

    c = sorted(C(l).items())

    res = 0
    j = 0
    for hi, ni in c:
        h = min(hi - j, ni) + j
        res += (hi - 1) * ni
        if h > j:
            j = h
    max_val = max(l) if l else 0
    if j < max_val:
        res -= max_val - j

    print(res)


if __name__ == "__main__":
    # 示例：使用 n=10 运行一次
    main(10)