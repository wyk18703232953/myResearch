n = 10**5

def main(n):
    # 构造一个由 '1' 和 '0' 组成的字符串，长度为 n
    # 确定性规则：位置 i 上为 '0' 当且仅当 i 是 3 的倍数，否则为 '1'
    if n <= 0:
        s = "0"
    else:
        s = "".join('0' if i % 3 == 0 else '1' for i in range(1, n + 1))

    if s == '0':
        print(0)
    else:
        print("1" + "0" * s.count('0'))


if __name__ == "__main__":
    main(n)