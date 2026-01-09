def main(n):
    # 生成确定性的输入 a 和 b
    # a: 数字字符串，长度为 max(1, n)
    # b: 数字字符串，长度为 max(1, n//2)
    len_a = max(1, n)
    len_b = max(1, n // 2)

    a = ''.join(str((i * 7 + 3) % 10) for i in range(len_a))
    b = ''.join(str((i * 5 + 1) % 10) for i in range(len_b))

    # 原始逻辑开始
    if len(b) > len(a):
        l = [int(i) for i in a]
        l.sort()
        l = l[::-1]
        temp = [str(i) for i in l]
        s = ''.join(temp)
        # print(s)
        pass

    else:
        d = {}
        for i in a:
            if i not in d:
                d[i] = 1

            else:
                d[i] = d[i] + 1

        flag = 0
        new = ''

        def find(i):
            nonlocal flag, d
            if i in d and d[i] > 0:
                d[i] = d[i] - 1
                return i

            for j in range(int(i), -1, -1):
                flag = 1
                j = str(j)
                if j in d and d[j] > 0:
                    d[j] = d[j] - 1
                    return j

        def fun(d_local):
            l_local = []
            for key in d_local:
                if d_local[key] > 0:
                    l_local = l_local + [int(key)] * d_local[key]
            l_local.sort()
            l_local = l_local[::-1]
            temp_local = [str(i) for i in l_local]
            s_local = ''.join(temp_local)
            return s_local

        def fun2(x):
            nonlocal new, d
            for i in range(x - 1, -1, -1):
                temp_local = new[i]
                for j in range(int(temp_local) - 1, -1, -1):
                    j_str = str(j)
                    if j_str in d and d[j_str] > 0:
                        new = new[:i] + j_str
                        d[j_str] = d[j_str] - 1
                        d[temp_local] = d[temp_local] + 1
                        return new
                d[temp_local] = d[temp_local] + 1

        for i in range(len(b)):
            if flag == 0:
                temp = find(b[i])
                if temp is None:
                    new = fun2(i)
                    new = new + fun(d)
                    break

                else:
                    new = new + temp

            else:
                new = new + fun(d)
                break

        # print(new)
        pass
if __name__ == "__main__":
    main(10)