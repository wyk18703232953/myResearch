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
                if pro == True:
                    if a[i] < b[0]:
                        pro = False
                m = c(n, b[1:], l-1, ans+str(a[i]), pro)
                n = a[:]
                if m != None:
                    if mx == None:
                        mx = int(m)
                    elif mx < int(m):
                        mx = int(m)
            elif not(pro):
                a.sort(reverse=True)
                a = list(map(str, a))
                return ans + ''.join(a)

            else:
                break
        return mx

    else:
        return ans


def original_logic(a_str, b_str):
    a = a_str
    b = b_str
    l = len(a)
    if len(a) != len(b):
        a_list = list(a)
        a_list.sort()
        return ''.join(a_list[::-1])

    else:
        a_list = list(map(int, a))
        b_list = list(map(int, b))
        a_list.sort()
        n = a_list[:]
        mx = 0
        prosh = -1
        for i in range(l):
            if a_list[i] == prosh:
                continue
            elif a_list[i] != 0 and a_list[i] <= b_list[0]:
                n.pop(i)
                prosh = a_list[i]
                pro = False
                if a_list[i] == b_list[0]:
                    pro = True
                m = c(n, b_list[1:], l-1, str(a_list[i]), pro)
                n = a_list[:]
                if m != None:
                    if mx < int(m):
                        mx = int(m)
            elif a_list[i] > b_list[0]:
                break
        return str(mx)


def main(n):
    if n <= 0:
        n = 1
    # 生成两个长度为 n 的数字串，完全确定性
    # a_str: 通过 (i % 10)
    # b_str: 通过 ((i * 7 + 3) % 10)
    a_digits = [(i % 10) for i in range(n)]
    b_digits = [((i * 7 + 3) % 10) for i in range(n)]
    a_str = ''.join(str(d) for d in a_digits)
    b_str = ''.join(str(d) for d in b_digits)
    result = original_logic(a_str, b_str)
    # print(result)
    pass
if __name__ == "__main__":
    main(5)