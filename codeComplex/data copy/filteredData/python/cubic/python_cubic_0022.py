def main(n):
    # 生成长度为 n 的确定性字符串：周期为 26 的小写字母序列
    string = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    n_len = len(string)
    check = True
    for sub_len in range(n_len - 1, 0, -1):
        for starting_index in range(n_len - sub_len + 1):
            if string[starting_index:starting_index + sub_len] in string[starting_index + 1:]:
                # print(sub_len)
                pass
                check = False
                break
        if not check:
            break
    if check:
        # print(0)
        pass
if __name__ == "__main__":
    main(1000)