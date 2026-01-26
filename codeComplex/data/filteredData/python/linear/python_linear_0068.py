def main(n):
    # 在原题中：第一行输入为 n, s，接下来有 n 行，每行 f, t
    # 这里将规模 n 映射为“操作次数”，并构造一个与 n 一致的 s 和 (f, t) 序列
    #
    # 构造方式完全确定性：
    #   s = n
    #   第 i 次循环 (i 从 0 到 n-1)：
    #       f = i % (n + 1)
    #       t = i * 2 + 1
    #
    # 这样可以保证：
    #   - 对每个 n，生成的数据唯一确定
    #   - 规模大致与 n 成正比，适合复杂度实验

    s = n
    ans = s

    for i in range(n):
        f = i % (n + 1)
        t = i * 2 + 1
        if t > (s - f):
            delta = t - (s - f)
            ans += delta
            s += delta

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：用 n = 10 进行一次运行
    main(10)