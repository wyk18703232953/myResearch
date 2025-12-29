import random

def c(a, b, l, ans, pro):
    if l != 0:
        n = a[:]
        mx = None
        pro1 = pro
        prosh = None
        for i in range(l):
            pro = pro1
            if a[i] == prosh:
                continue
            elif (a[i] <= b[0] and pro):
                n.pop(i)
                prosh = a[i]
                if pro:
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
    """
    n: 规模，表示数字串长度
    生成两个长度为 n 的数字串 a, b，模仿原始 input 行为并运行原逻辑。
    返回程序本应打印的结果（字符串形式）。
    """

    # 生成测试数据：
    # a, b 为长度为 n 的数字串，允许前导 0，以与原逻辑兼容
    a_str = ''.join(str(random.randint(0, 9)) for _ in range(n))
    b_str = ''.join(str(random.randint(0, 9)) for _ in range(n))

    a = a_str
    b = b_str
    l = len(a)

    if len(a) != len(b):
        a_list = list(a)
        a_list.sort()
        result = ''.join(a_list[::-1])
        return result

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

    return str(mx)


if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    print(main(5))