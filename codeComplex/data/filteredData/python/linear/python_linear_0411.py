def main(n):
    # 根据 n 生成确定性输入：
    # a: 未在核心逻辑中使用，固定为 0
    # b: 需要选择的字符数，限定在 1..26 内
    # c: 从字母表前 m 个字母构造的字符串，其中 m >= b，且受 n 控制
    lis = "abcdefghijklmnopqrstuvwxyz"
    if n <= 0:
        n = 1
    b = (n % 26) + 1
    m = b + (n % (27 - b))  # 保证 b <= m <= 26
    c = lis[:m]
    su = 0
    cnt = 0
    j = -2
    i = 0
    while i < 26 and cnt < b:
        if lis[i] in c and i - 2 >= j:
            su += i + 1
            cnt += 1
            j = i
        i += 1
    if cnt < b:
        print(-1)
    else:
        print(su)


if __name__ == "__main__":
    main(10)