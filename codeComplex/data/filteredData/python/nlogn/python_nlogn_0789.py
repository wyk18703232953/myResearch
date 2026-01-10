def main(n):
    # 映射：n 表示数组长度，k 固定为 n//2 + 1（至少为 1）
    if n <= 0:
        return
    k = n // 2 + 1
    if k < 1:
        k = 1

    # 确定性生成数组 a：严格递增，便于保持原逻辑
    # 例：a[i] = 3 * i + (i % 5)
    a = [3 * i + (i % 5) for i in range(n)]

    diff = []
    if n == 1:
        print(0)
    else:
        for i in range(n - 1):
            diff.append(a[i + 1] - a[i])

        diff.sort(reverse=True)
        ans = a[-1] - a[0]
        for i in range(min(k - 1, len(diff))):
            ans -= diff[i]

        print(ans)


if __name__ == "__main__":
    # 示例调用：可以修改这里的 n 来做规模化实验
    main(10)