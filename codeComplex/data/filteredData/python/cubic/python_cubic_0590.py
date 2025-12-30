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
    # 生成测试数据：
    # a 为长度 n 的数字串（允许前导 0），b 为长度为 len(a) 或略大的数字串
    # 使得程序逻辑可以运行。
    import random

    # 生成 a：n 位数字
    a = "".join(str(random.randint(0, 9)) for _ in range(n))

    # 为了覆盖两种分支，生成 b 的长度在 [n-1, n+1] 之间（至少为 1）
    len_b = max(1, n + random.choice([-1, 0, 1]))
    # 为避免 b 太小/太大导致 trivial，直接生成一个同位数随机数
    b = "".join(str(random.randint(0, 9)) for _ in range(len_b))

    chars = [i for i in a]
    chars.sort()

    if len(a) < len(b):
        result = "".join(chars[::-1])
    else:
        result = find_number(b, chars)

    # 输出结果，可根据需要返回
    print("a =", a)
    print("b =", b)
    print("result =", result)
    return result


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)