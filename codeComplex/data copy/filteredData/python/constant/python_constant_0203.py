def main(n):
    # 输入规模含义：生成长度为 n 的整数列表 k
    # 确定性生成规则：k[i] = (i % 5) + 1
    k = [(i % 5) + 1 for i in range(n)]

    ans = 'NO'
    if min(k) == 1 or k.count(2) >= 2 or k.count(3) >= 3 or (k.count(4) == 2 and k.count(2) == 1):
        ans = 'YES'

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)