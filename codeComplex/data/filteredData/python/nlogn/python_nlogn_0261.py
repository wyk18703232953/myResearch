def main(n):
    def fn(s, e, qs, qe):
        if qs <= s <= e <= qe:
            return True
        return False

    # 输入规模 n 表示区间数量
    # 构造 n 个确定性的区间 [l, r]
    # 规律：l = i, r = i + (i % 3) + 1，保证有一定概率出现包含关系
    a = [[i, i + (i % 3) + 1, i] for i in range(n)]

    ans = [-1, -1]
    a.sort(key=lambda x: (x[0], x[1]))
    for i in range(n - 1):
        if fn(a[i][0], a[i][1], a[i + 1][0], a[i + 1][1]):
            ans = [a[i][2] + 1, a[i + 1][2] + 1]
            break
        elif fn(a[i + 1][0], a[i + 1][1], a[i][0], a[i][1]):
            ans = [a[i + 1][2] + 1, a[i][2] + 1]
            break

    print(*ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 以进行时间复杂度实验
    main(10)