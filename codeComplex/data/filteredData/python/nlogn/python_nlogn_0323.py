def main(n):
    # 生成确定性输入：长度为 n 的数组 a
    # 规则：a[i] = (i % (n // 2 + 1)) + 1 保证有重复和部分匹配
    if n <= 0:
        return
    a = [(i % (n // 2 + 1)) + 1 for i in range(n)]

    if sum(a[i] == i + 1 for i in range(n)) >= n // 1000:
        print("Petr")
    else:
        print("Um_nik")


if __name__ == "__main__":
    # 示例：使用 n = 10**6 进行时间复杂度实验
    main(10**6)