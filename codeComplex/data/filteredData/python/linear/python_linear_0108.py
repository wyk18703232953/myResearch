def main(n):
    # 生成确定性输入：两个字符串 s1 和 s2
    # s1 长度为 n，s2 长度为 max(1, n//2)
    if n <= 0:
        s1 = "a"
        s2 = "b"

    else:
        # s1: 从 'a' 开始循环到 'z'
        s1 = "".join(chr(ord('a') + (i % 26)) for i in range(n))
        # s2: 从 'm' 开始循环到 'z' 再从 'a' 开始
        m = max(1, n // 2)
        s2 = "".join(chr(ord('m') + (i % 26)) if ord('m') + (i % 26) <= ord('z')
                     else chr(ord('a') + (ord('m') + (i % 26) - ord('z') - 1))
                     for i in range(m))

    s1_str = s1
    s2_str = s2

    res = s1_str[0]
    flag = 0
    for i in range(1, len(s1_str)):
        if s1_str[i] >= s2_str[0]:
            res += s2_str[0]
            flag = 1
            break

        else:
            res += s1_str[i]
    if flag == 0:
        res += s2_str[0]
    # print(res)
    pass
if __name__ == "__main__":
    main(10)