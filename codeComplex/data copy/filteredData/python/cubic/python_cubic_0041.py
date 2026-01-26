def cic(my_string):
    my_hash = set()
    max_v = -1 << 256
    for i in range(len(my_string)):
        empty = my_string[i] + ''
        if empty in my_hash:
            max_v = max(max_v, len(empty))

        else:
            my_hash.add(empty)
        for j in range(i + 1, len(my_string)):
            empty += my_string[j]
            if empty not in my_hash:
                my_hash.add(empty)

            else:
                max_v = max(max_v, len(empty))
    return 0 if max_v < 0 else max_v


def main(n):
    # 根据规模 n 生成测试数据：长度为 n 的小写字母字符串
    # 示例生成方式：循环使用 'a' 到 'z'
    from string import ascii_lowercase
    letters = ascii_lowercase
    my_string = ''.join(letters[i % 26] for i in range(n))
    # print(cic(my_string))
    pass
if __name__ == '__main__':
    # 示例：调用 main(10)，实际使用中可根据需要修改 n
    main(10)