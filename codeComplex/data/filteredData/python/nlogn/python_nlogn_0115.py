def main(n):
    # 生成确定性输入数据：长度为 n 的整数数组
    # 示例构造：a[i] = (i * 3 + 1) % (n + 5)
    a = [(i * 3 + 1) % (n + 5) for i in range(n)]

    sortm = a[:]  # 拷贝原数组
    sortm.sort()

    cnt = 0
    for i in range(n):
        if a[i] != sortm[i]:
            cnt += 1

    if cnt <= 2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main(10)