def main(n):
    # n 作为数组长度，生成确定性测试数据
    # x 取固定值，保证与位运算有关
    if n <= 0:
        return
    x = 10  # 固定位与掩码
    # 生成长度为 n 的数组 a，元素两两不同（避免一开始就 len(set(a)) != n）
    a = [(i * 3 + 7) % (2 * n + 5) for i in range(n)]

    ans = 0
    s = set(a)
    if len(s) != n:
        print(0)
        return
    for i in range(n):
        v = a[i]
        a[i] &= x
        if a[i] in s and v != a[i]:
            ans = 1
            break
    if ans == 1:
        print(1)
    elif len(set(a)) == n:
        print(-1)
    else:
        print(2)


if __name__ == "__main__":
    # 示例调用
    main(10)