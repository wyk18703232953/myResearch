def main(n):
    # 生成确定性输入：长度为 n 的整数列表 a
    # 定义规则：a[i] = (i % (n // 2 + 1)) + 1 保证有一定数量的 a[i] == i+1，但不全相等
    if n <= 0:
        return
    a = [(i % (n // 2 + 1)) + 1 for i in range(n)]
    w = sum(a[i] == i + 1 for i in range(n))
    if w >= n // 1000:
        # print("Petr")
        pass

    else:
        # print("Um_nik")
        pass
if __name__ == "__main__":
    main(1000000)