def main(n):
    # 这里根据 n 生成测试数据 (a, b)，示例策略：
    # - 若 n == 1：令 a = 1, b = 1
    # - 若 n == 2：令 a = 2, b = 1
    # - 若 n == 3：令 a = 1, b = 2
    # - 其他：令 a = 1, b = 1
    if n == 1:
        a, b = 1, 1
    elif n == 2:
        a, b = 2, 1
    elif n == 3:
        a, b = 1, 2

    else:
        a, b = 1, 1

    if a != 1 and b != 1:
        # print("NO")
        pass

    else:
        con_char = '1'
        discon_char = '0'
        if a == 1:
            con_char = '0'
            discon_char = '1'
            t = a
            a = b
            b = t

        if a > 1:
            # print("YES")
            pass
            n_con = n - a + 1
            for i in range(n):
                res = []
                for j in range(n):
                    if i == j:
                        res.append('0')
                    elif i < n_con and j < n_con:
                        res.append(con_char)

                    else:
                        res.append(discon_char)
                # print(''.join(res))
                pass

        else:
            if n == 1 or n > 3:
                # print("YES")
                pass
                for i in range(n):
                    res = []
                    for j in range(n):
                        if i == j:
                            res.append('0')
                        elif abs(i - j) == 1:
                            res.append('1')

                        else:
                            res.append('0')
                    # print(''.join(res))
                    pass

            else:
                # print("NO")
                pass