def smallest(d):
    out = ""
    for j in range(0, 10):
        out += ("%d" % j) * d[j]
    return out


def largest(d):
    out = ""
    for j in range(9, -1, -1):
        out += ("%d" % j) * d[j]
    return out


def solve(sa, sb):
    b = int(sb)
    h = int(sa)

    digits_a = [0] * 10
    while h > 0:
        digits_a[h % 10] += 1
        h //= 10

    if len(sb) > len(sa):
        return largest(digits_a)

    out = 0
    for i in range(len(sa) - 1, -1, -1):
        for j in range(9, -1, -1):
            if digits_a[j] == 0:
                continue

            bj = (b % (10 ** (i + 1))) // (10 ** i)

            if j < bj:
                digits_a[j] -= 1
                if out > 0:
                    return "{}{}{}".format(out, j, largest(digits_a))

                else:
                    return "{}{}".format(j, largest(digits_a))

            if j == bj:
                if i == 0:
                    out = 10 * out + j
                    return str(out)
                digits_a[j] -= 1
                if int(smallest(digits_a)) <= b % (10 ** i):
                    out = 10 * out + j
                    break

                else:
                    digits_a[j] += 1

    return str(out)


def main(n):
    # 依据规模 n 生成测试数据：
    # sa 为一个长度为 n 的数字串（不含前导零）
    # sb 为一个长度为 n 的数字串（保证是整数且不含前导零）
    if n <= 0:
        return ""

    # 生成 sa
    sa = "1" + "2" * (n - 1)  # 简单构造：例如 n=3 -> "122"
    # 生成 sb，比 sa 稍大一些，保证同长度
    # 如果 n=1，sa="1"，sb="9"
    if n == 1:
        sb = "9"

    else:
        sb = "9" * n

    result = solve(sa, sb)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例：调用 main，n 可按需调整
    main(5)