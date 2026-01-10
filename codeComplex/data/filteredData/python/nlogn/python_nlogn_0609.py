def main(n):
    # 数据规模设计：
    # n 表示数组长度
    # m 设置为 n 的一个简单函数（但原程序未使用 m，仅保持结构）
    m = n * 2 + 1

    # 构造确定性数组 a，元素大小随 n 缩放，保证有一定变化和重复
    # 示例：a[i] = (i % 7) + (i // 3) + 1
    a = [(i % 7) + (i // 3) + 1 for i in range(n)]

    s = sum(a)
    need = 0
    a.sort()
    j = 1
    flag = 0
    k = max(a) if a else 0
    if n == 1:
        result = 0
    else:
        for i in range(n):
            if a[i] < j:
                flag = 1
            else:
                flag = 0
            if a[i] == 1:
                need += 1
            elif a[i] >= j and i != n - 1:
                need += 1
            elif a[i] >= j and i == n - 1 and j <= k:
                need += k - j + 1
            else:
                need += 1
            if flag != 1:
                j += 1
        result = s - need

    print(result)


if __name__ == "__main__":
    # 示例规模调用，可根据需要修改 n 以做时间复杂度实验
    main(10)