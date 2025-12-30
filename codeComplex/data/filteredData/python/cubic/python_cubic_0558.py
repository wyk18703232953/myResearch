def dig(d):
    return ord(d) - ord('0')


def biggest_left(counts):
    res = ''
    for i in range(9, -1, -1):
        res += str(i) * counts[i]
    return res


def ok(d, _counts, rest):
    if rest == '':
        return True

    counts = _counts.copy()
    counts[d] -= 1

    r = ''
    for i in range(10):
        r += str(i) * counts[i]

    return int(r) <= int(rest)


def solve(a, b):
    counts = [0] * 10
    for d in a:
        counts[dig(d)] += 1

    ans = ''
    if len(a) < len(b):
        return biggest_left(counts)

    n = len(a)
    for i in range(n):
        d = dig(b[i])

        if counts[d] and ok(d, counts, b[i+1:]):
            ans += b[i]
            counts[d] -= 1
        else:
            for s in range(d-1, -1, -1):
                if counts[s] > 0:
                    ans += str(s)
                    counts[s] -= 1
                    ans += biggest_left(counts)
                    return ans
    return ans


def main(n):
    # 根据规模 n 生成测试数据：
    # 生成一个长度为 n 的数字串 a（0-9 随机），
    # 再生成一个不小于 a 的 b（这里简单地设为按字典序略大的串）。
    import random

    if n <= 0:
        print("")
        return

    # 生成 a
    a_digits = [str(random.randint(0, 9)) for _ in range(n)]
    a = "".join(a_digits)

    # 为了尽量让 b >= a，构造 b：
    # 复制 a，然后随机在若干位置增加一点数值（不进位构造）
    b_list = list(a_digits)
    # 随机选择若干位置进行“增加”，避免全是 9
    for i in range(n):
        if b_list[i] != '9' and random.random() < 0.3:
            b_list[i] = str(int(b_list[i]) + 1)
    b = "".join(b_list)

    ans = solve(a, b)
    print(ans)


if __name__ == '__main__':
    # 示例：调用 main，n 为规模（长度）
    main(5)