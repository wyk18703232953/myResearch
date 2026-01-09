def main(n):
    # n 表示字符串长度规模
    if n <= 0:
        return

    # 构造确定性的 a 和 b，长度均为 n
    # 字符来源于 '0'~'9' 和 'A'~'Z'
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    m = len(chars)

    a = ''.join(chars[i % m] for i in range(n))
    b = ''.join(chars[(i * 7 + 3) % m] for i in range(n))

    if len(a) < len(b):
        a_list = list(a)
        a_list.sort(reverse=True)
        # print(''.join(a_list))
        pass
        return

    def solve(i, a_list: list):
        if i == len(b):
            return ''
        if b[i] in a_list:
            a_list.remove(b[i])
            suf = solve(i + 1, a_list)
            if suf is not None:
                return b[i] + suf
            a_list.append(b[i])
        best = ''
        for c in a_list:
            if c < b[i] and c > best:
                best = c
        if best == '':
            return None
        a_list.remove(best)
        a_list.sort(reverse=True)
        return best + ''.join(a_list)

    a_list = list(a)
    result = solve(0, a_list)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 进行规模实验
    main(10)