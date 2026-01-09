def is_pal(s):
    if s == s[::-1]:
        return True

    else:
        return False

def core_logic(s):
    if not is_pal(s):
        return len(s)

    else:
        not_eq = False
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                not_eq = True
                return len(s) - 1
        if not not_eq:
            return 0

def main(n):
    # 生成确定性字符串，长度为 n
    # 字符序列周期性为 26 个小写字母
    chars = [chr(ord('a') + (i % 26)) for i in range(n)]
    s = "".join(chars)
    result = core_logic(s)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)