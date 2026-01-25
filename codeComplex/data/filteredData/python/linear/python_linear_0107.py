def main(n):
    # 生成确定性的输入
    # str1: 由 'a' 到 'z' 循环构成的长度为 n 的字符串
    str1 = ''.join(chr(ord('a') + (i % 26)) for i in range(max(1, n)))
    # str2: 固定为单字符，体现原程序使用场景
    str2 = 'm'

    # 原程序核心逻辑
    lst = []
    lst_ans = []
    l_count = 0
    count = 0
    for i in str2:
        if count < 1:
            lst.append(i)
        else:
            break
    for i in str1:
        if count == 0:
            lst_ans.append(i)
            count += 1
        elif ord(i) < ord(lst[0]):
            lst_ans.append(i)
        else:
            lst_ans.append(lst[0])
            break
    else:
        lst_ans.append(lst[0])
    print(''.join(lst_ans))


if __name__ == "__main__":
    main(10)