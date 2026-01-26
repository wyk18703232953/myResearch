def main(n):
    # 参数含义映射：
    # n: 元素个数
    # l, r: 允许的和区间
    # x: 最小值与最大值的差的下限
    if n <= 0:
        return 0

    # 确定性生成参数
    l = n
    r = 3 * n
    x = max(1, n // 4)

    # 确定性生成数组：严格递增，便于控制 max-min
    arr = [i + 1 for i in range(n)]

    res = 0
    for j in range(1, 2 ** n):
        a = [arr[i] for i in range(n) if ((j >> i) & 1) == 1]
        s = sum(a)
        if max(a) - min(a) >= x and l <= s <= r:
            res += 1
    return res


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的规模
    print(main(10))