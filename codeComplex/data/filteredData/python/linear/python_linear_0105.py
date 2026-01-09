def main(n):
    if n < 1:
        return
    # 生成两个字符串 s1, s2，长度与 n 相关且可重复确定
    # s1 长度为 n，字符按循环 'a' 到 'z' 生成
    s1 = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    # s2 为一个非空字符串，这里固定为长度 1，字符依据 n 生成
    s2 = chr(ord('a') + (n % 26))
    ans = s1[0]
    for i in range(1, len(s1)):
        if s1[i] < s2[0]:
            ans += s1[i]
            if i == len(s1) - 1:
                ans += s2[0]

        else:
            ans += s2[0]
            break
    if len(s1) == 1:
        # print(s1[0] + s2[0])
        pass

    else:
        # print(ans)
        pass
if __name__ == "__main__":
    main(10)