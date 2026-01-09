def main(n):
    # 生成确定性的字符串 m，长度至少为 n
    # 构造一个周期为 3 的模式，保证有 0 和 1
    base_pattern = ['1', '0', '1']
    s = [base_pattern[i % 3] for i in range(n)]
    m = ''.join(s)

    s_list = list(m)

    if n == 1:
        ans = s_list[0]

    else:
        count = 0
        for i in range(0, n):
            if s_list[i] == '0':
                count = count + 1
        ans = '1'
        for _ in range(0, count):
            ans = ans + '0'

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)