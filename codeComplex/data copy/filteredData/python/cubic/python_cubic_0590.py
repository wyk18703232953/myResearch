def make_number(b, chars):
    if len(chars) == 0:
        return ""
    target = chars[0]
    for i in chars:
        if int(b[0]) <= int(i):
            break
        target = i
    chars.remove(target)
    return target + "".join(chars[::-1])


def find_number(b, chars):
    backup_chars = list(chars)
    if len(b) == 1:
        return chars[0]
    elif b[0] in chars:
        chars.remove(b[0])
        num = b[0] + find_number(b[1:], chars)
        if min(num, b) == b and b != num:
            return make_number(b, backup_chars)

        else:
            return num

    else:
        return make_number(b, backup_chars)


def main(n):
    # 生成确定性的输入 a 和 b
    # a 为长度为 n 的数字串，字符来自 '0'..'9'
    a_chars = [str(i % 10) for i in range(n)]
    a = "".join(a_chars)

    # b 的长度与 a 相同，用另一种确定性方式生成
    b_chars = [str((i * 3 + 1) % 10) for i in range(n)]
    b = "".join(b_chars)

    chars = [i for i in a]
    chars.sort()

    if len(a) < len(b):
        # print("".join(chars[::-1]))
        pass

    else:
        # print(find_number(b, chars))
        pass
if __name__ == "__main__":
    main(10)