def c(a, b, l, ans, pro):
    if l != 0:
        n = a[:]
        mx = None
        pro1 = pro
        prosh = set()
        for i in range(l):
            pro = pro1
            if a[i] == prosh:
                continue
            elif (a[i] <= b[0] and pro):
                n.pop(i)
                prosh = a[i]
                if pro is True:
                    if a[i] < b[0]:
                        pro = False
                m = c(n, b[1:], l - 1, ans + str(a[i]), pro)
                n = a[:]
                if m is not None:
                    if mx is None:
                        mx = int(m)
                    elif mx < int(m):
                        mx = int(m)
            elif not pro:
                a.sort(reverse=True)
                a = list(map(str, a))
                return ans + ''.join(a)

            else:
                break
        return mx

    else:
        return ans


def main(n):
    # 生成确定性的输入字符串 a 和 b，长度均为 n
    # a 是从 0 到 9 循环的数字串
    # b 是从 9 到 0 逆向循环的数字串
    digits_a = [str(i % 10) for i in range(n)]
    digits_b = [str((9 - (i % 10))) for i in range(n)]
    a_str = ''.join(digits_a)
    b_str = ''.join(digits_b)

    a = a_str
    b = b_str
    l = len(a)
    if len(a) != len(b):
        a_list = list(a)
        a_list.sort()
        result = ''.join(a_list[::-1])
        # print(result)
        pass

    else:
        a_list = list(map(int, a))
        b_list = list(map(int, b))
        a_list.sort()
        n_list = a_list[:]
        mx = 0
        prosh = -1
        for i in range(l):
            if a_list[i] == prosh:
                continue
            elif a_list[i] != 0 and a_list[i] <= b_list[0]:
                n_list.pop(i)
                prosh = a_list[i]
                pro = False
                if a_list[i] == b_list[0]:
                    pro = True
                m = c(n_list, b_list[1:], l - 1, str(a_list[i]), pro)
                n_list = a_list[:]
                if m is not None:
                    if mx < int(m):
                        mx = int(m)
            elif a_list[i] > b_list[0]:
                break
        # print(mx)
        pass
if __name__ == "__main__":
    main(10)