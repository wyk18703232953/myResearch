def main(n):
    # 为了实现可规模化的实验，这里将原程序中的两个输入：
    # n: 循环上界
    # s: 被反复整除与取模的数
    #
    # 统一由单一规模参数 n 确定性生成。
    # 选择 s = n * (n + 1)，保证随着 n 增大，s 也按二次规模增长。
    s = n * (n + 1)
    res = 0
    for i in range(n, 0, -1):
        res += s // i
        s = s % i
    return res


if __name__ == "__main__":
    # 示例调用，可按需修改 n 来做时间复杂度实验
    print(main(10))