def main(n):
    # 对于时间复杂度分析，将 n 视为要生成的测试用例数量
    # 第 i 个用例为一对 (l, r)，满足 0 <= l <= r
    # 构造方式保证确定性
    results = []
    for i in range(1, n + 1):
        # 构造区间 [l, r]
        # 选择一个随 i 线性增长的区间长度
        length = i  # 区间长度约为 i
        l = i * i   # 起点随 i^2 增长
        r = l + length
        # 核心算法逻辑与原 solve 中相同
        s1 = bin(l)[2:]
        s2 = bin(r)[2:]
        if len(s1) != len(s2):
            x = (1 << len(s2)) - 1
            results.append(x)
            continue
        x = 0
        for bit in range(62, -1, -1):
            if ((l >> bit) & 1) ^ ((r >> bit) & 1):
                x += (1 << (bit + 1))
                x -= 1
                break
        results.append(x)
    return results


if __name__ == "__main__":
    # 示例：运行规模为 10
    output = main(10)
    for val in output:
        # print(val)
        pass