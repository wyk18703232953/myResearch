def main(n):
    # 生成确定性输入：n 个整数（可能有重复），构造一个字符串 s
    # 数值分布：i % (n//2 + 1)，保证有重复且有序可预测
    if n <= 0:
        return
    values = [i % (n // 2 + 1) for i in range(n)]
    s = " ".join(str(x) for x in values)

    # 原始逻辑开始
    L = s.split(" ")
    L = list(set(L))
    for i in range(len(L)):
        L[i] = int(L[i])
    L = sorted(L)
    if len(L) == 1:
        print("NO")
    else:
        print(L[1])


if __name__ == "__main__":
    main(10)