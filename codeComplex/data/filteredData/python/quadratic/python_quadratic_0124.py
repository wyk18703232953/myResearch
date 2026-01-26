def main(n):
    # 解释规模映射：
    # n >= 2 时，假定有 n 个元素，m 也等于 n
    # 构造 a 为 1..n 的循环序列，保证每个位置出现次数尽可能均匀
    if n <= 0:
        return 0
    m = n
    count = [0] * n
    # 构造一个确定性的 a（1 到 n 的循环）
    a = [(i % n) + 1 for i in range(m)]
    for i in range(m):
        count[a[i] - 1] += 1
    result = min(count)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 以做规模实验
    main(10)