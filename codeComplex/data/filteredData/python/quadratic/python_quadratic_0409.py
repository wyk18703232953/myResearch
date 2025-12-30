def main(n: int) -> str:
    # 生成长度为 n 的测试串，这里用周期性模式方便测试
    # 示例：n=7 -> "abcabca"
    base = "abc"
    t = (base * (n // len(base) + 1))[:n]

    # 设定重复次数 k，可根据需要调整，这里给一个与 n 相关的值
    k = max(1, n // 3)

    j = 0
    for i in range(1, n):
        if t[:i] == t[-i:]:
            j = i
    s = t + (k - 1) * t[-(n - j):]
    return s


if __name__ == "__main__":
    # 示例运行：n = 10
    print(main(10))