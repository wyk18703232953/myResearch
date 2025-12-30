import random

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
    # 生成规模为 n 的测试数据：a_str 和 b_str 为长度为 n 的数字串
    # 确保无前导零的情况有意义：首位数字非零
    digits = "0123456789"

    def gen_number(length):
        if length == 0:
            return ""
        first = random.choice(digits[1:])  # 首位不为 0
        rest = [random.choice(digits) for _ in range(length - 1)]
        return first + "".join(rest)

    a = gen_number(n)
    b = gen_number(n)

    l = len(a)
    if len(a) != len(b):
        a_list = list(a)
        a_list.sort()
        result = ''.join(a_list[::-1])
        print(result)
        return result
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
        print(mx)
        return mx


# 示例调用
if __name__ == "__main__":
    # 例如 n = 5
    main(5)