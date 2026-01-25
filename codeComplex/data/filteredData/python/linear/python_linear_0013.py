def main(n):
    # 映射：n 作为原程序中的 n，k 设为 n//2（与规模线性相关且确定）
    k = n // 2

    v = []
    for i in range(2, n + 1):
        if all(i % j != 0 for j in v):
            v.append(i)

    c = 0
    for i in range(len(v) - 1):
        if 1 + v[i] + v[i + 1] in v:
            c += 1

    if c >= k:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 进行时间复杂度实验
    main(1000)