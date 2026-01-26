def check(e, value, pre, b, maxi_ref):
    e[str(value)] -= 1
    pre += str(value)
    arr = []
    for k in e:
        for _ in range(e[k]):
            arr.append(k)
    arr.sort(reverse=True)
    st = ''.join(arr)
    alpha = int(pre + st)
    if alpha <= int(b):
        maxi_ref[0] = max(maxi_ref[0], alpha)


def main(n):
    """
    规模 n 用来生成测试数据:
    - 生成一个长度为 n 的数字串 a（从 0..9 循环）
    - 生成一个长度为 n 或 n+1 的数字串 b，使得 b >= a
    """
    # 生成测试数据 a, b
    a = ''.join(str(i % 10) for i in range(n))
    # 让 b 稍微大一些：对 a 的第一个数字 +1 (若是 '9' 则变 '8'，然后首位补 '1')
    if a and a[0] != '9':
        b = str(int(a[0]) + 1) + a[1:]

    else:
        # 避免首位'9'进位复杂，简单构造一个比 a 更长的串
        b = '1' + a

    d = {}
    for ch in a:
        d[ch] = d.get(ch, 0) + 1

    maxi_ref = [0]
    num = ""

    if len(a) < len(b):
        check(d.copy(), max(d), '', b, maxi_ref)

    else:
        for i in b:
            if i in d and d[i] > 0:
                for j in range(int(i) - 1, -1, -1):
                    if str(j) in d and d[str(j)] > 0:
                        check(d.copy(), j, num, b, maxi_ref)
                        break
                check(d.copy(), i, num, b, maxi_ref)
                num += i
                d[i] -= 1

            else:
                for j in range(int(i) - 1, -1, -1):
                    if str(j) in d and d[str(j)] > 0:
                        check(d.copy(), j, num, b, maxi_ref)
                        break
                break

    # print(maxi_ref[0])
    pass
if __name__ == "__main__":
    # 示例：调用 main(5)，你可以在外部修改 n 测试不同规模
    main(5)