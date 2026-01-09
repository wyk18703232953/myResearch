def main(n):
    # 生成确定性输入：n 对 (f, t)，以及 s
    s = n  # 将原始的 s 设置为与规模 n 相关的一个确定性值
    ans = s
    for i in range(n):
        f = i
        t = i * 2
        ans = max(ans, t + f)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)