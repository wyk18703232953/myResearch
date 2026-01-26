def main(n):
    # 确定性生成输入数据
    if n <= 0:
        n = 1
    d = 3
    lst = [i * 2 for i in range(n)]
    # 核心逻辑保持不变
    lst.sort()
    Ans = 2
    for i in range(1, n):
        if lst[i] - lst[i - 1] > 2 * d:
            Ans += 2
        elif lst[i] - lst[i - 1] == 2 * d:
            Ans += 1
    # print(Ans)
    pass
if __name__ == "__main__":
    main(10)