def sol(n, m):
    v = [0 for _ in range(n + 1)]
    left, right = 1, n
    for i in range(1, n + 1):
        if n - i - 1 <= 0:
            pw = 1
        else:
            pw = 1 << (n - i - 1)

        if m <= pw:
            v[left] = i
            left += 1
        else:
            v[right] = i
            right -= 1
            m -= pw
    return [' '.join(map(str, v[1:]))]


def main(n):
    # 将 n 解释为原程序中的 n，m 由 n 确定性构造
    # 这里构造 m = max(1, n // 2)，完全确定且可规模化
    if n <= 0:
        return []
    m = max(1, n // 2)
    return sol(n, m)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的规模
    n = 10
    for line in main(n):
        print(line)