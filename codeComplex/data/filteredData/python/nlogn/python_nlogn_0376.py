def main(n):
    # 解释输入规模映射：
    # n -> 数组长度
    # k -> 与 n 相关的一个确定性值，这里设为 n // 3 + 1
    k = n // 3 + 1

    # 生成确定性数组 a，长度为 n
    # 为了制造重复元素和间隔，使用一个简单的算术构造
    a = [(i // 3) * (k // 2 + 1) for i in range(n)]

    # 原始逻辑开始
    a = sorted(a)

    cur_v = a[0]
    cur_count = 1
    ans = 0

    for i in range(1, len(a)):
        if a[i] > a[i - 1] and a[i] > a[i - 1] + k:
            ans += cur_count
            cur_count = 1
        elif a[i] == a[i - 1]:
            cur_count += 1
        elif a[i] > a[i - 1]:
            cur_count = 1

    ans += cur_count

    print(ans)


if __name__ == "__main__":
    # 示例调用：可按需修改 n 以进行不同规模的时间复杂度实验
    main(10)