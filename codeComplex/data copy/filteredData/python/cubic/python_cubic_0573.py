def get_smallest(m, l):
    res = ''
    for i in "0123456789":
        if m.get(i, 0):
            if i == l:
                res += i * (m[i] - 1)

            else:
                res += i * m[i]
    return res


def solve(a, b):
    if len(a) < len(b):
        a = sorted(a)
        a.reverse()
        return ''.join(a)
    elif a == b:
        return a

    else:
        cmap = dict()
        for i in a:
            cmap[i] = cmap.get(i, 0) + 1

        cur = 0
        res = ''
        gm = False

        while cur < len(a):
            for i in "9876543210":
                if cmap.get(i, 0):
                    if cur == len(a) - 1 or i < b[cur] or gm:
                        res += i
                        cmap[i] -= 1
                        gm = True
                        break
                    elif i == b[cur]:
                        if get_smallest(cmap, i) <= b[cur + 1:]:
                            res += i
                            cmap[i] -= 1
                            break
            cur += 1

        return res


def main(n):
    # 生成长度为 n 的数字串 a、b，使得逻辑有意义：
    # a 为从 0..9 循环生成的串；b 为同长度的非降序数字串
    digits = "0123456789"
    a = ''.join(digits[i % 10] for i in range(n))
    # b 生成为全 9 的串，确保 len(a) == len(b)，触发主分支逻辑
    b = '9' * n

    result = solve(a, b)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：运行规模 n = 10
    main(10)