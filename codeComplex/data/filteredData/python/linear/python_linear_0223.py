def main(n):
    # 保证 n 至少为 1
    if n <= 0:
        n = 1

    # 根据 n 构造输入字符串 m，长度为 n
    # 确定性规则：位置 i 上为 '0' 若 i 是偶数，否则为 '1'
    m = ''.join('0' if i % 2 == 0 else '1' for i in range(n))

    s = list(m)

    if n == 1:
        ans = s[0]

    else:
        count = 0
        for i in range(0, n):
            if s[i] == '0':
                count = count + 1
        ans = '1'
        for i in range(0, count):
            ans = ans + '0'

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用：可以修改这里的 n 来进行规模实验
    main(10)