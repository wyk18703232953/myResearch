def func(x1, y1, x2, y2, x3, y3):
    rect1 = [x1, y1]
    rect2 = [x2, y2]
    rect3 = [x3, y3]

    for i in rect1:
        for ii in rect2:
            for iii in rect3:
                recta = [x1, y1]
                rectb = [x2, y2]
                rectc = [x3, y3]

                if i == ii == iii:
                    rect1.remove(i)
                    rect2.remove(i)
                    rect3.remove(i)

                if rect1[0] + rect2[0] + rect3[0] == i:
                    # print(i)
                    pass
                    for j in range(i):
                        # print("A" * rect1[0] + "B" * rect2[0] + "C" * rect3[0])
                        pass
                    return

                rect1 = recta
                rect2 = rectb
                rect3 = rectc

    rect11 = [x1, y1]
    rect22 = [x2, y2]
    rect33 = [x3, y3]
    rect1 = [x1, y1]
    rect2 = [x2, y2]
    rect3 = [x3, y3]

    recta = [x1, y1]
    rectb = [x2, y2]
    rectc = [x3, y3]
    for i in rect11:
        for ii in rect22:
            for iii in rect33:
                if i == ii:
                    rect1.remove(i)
                    rect2.remove(ii)
                    if rect1[0] + rect2[0] == iii:
                        rect3.remove(iii)
                        if i + rect3[0] == iii:
                            # print(iii)
                            pass
                            for j in range(iii):
                                if j < rect1[0]:
                                    # print("C" * rect3[0] + "A" * i)
                                    pass

                                else:
                                    # print("C" * rect3[0] + "B" * ii)
                                    pass
                            return
                rect1 = recta.copy()
                rect2 = rectb.copy()
                rect3 = rectc.copy()

                if i == iii:
                    rect1.remove(i)
                    rect3.remove(iii)
                    if rect1[0] + rect3[0] == ii:
                        rect2.remove(ii)
                        if i + rect2[0] == ii:
                            # print(ii)
                            pass

                            for j in range(ii):
                                if j < rect1[0]:
                                    # print("B" * rect2[0] + "A" * i)
                                    pass

                                else:
                                    # print("B" * rect2[0] + "C" * iii)
                                    pass
                            return
                rect1 = recta.copy()
                rect2 = rectb.copy()
                rect3 = rectc.copy()

                if ii == iii:
                    rect2.remove(ii)
                    rect3.remove(iii)
                    if rect2[0] + rect3[0] == i:
                        rect1.remove(i)
                        if i == rect1[0] + ii:
                            # print(i)
                            pass
                            for j in range(i):
                                if j < rect2[0]:
                                    # print("A" * rect1[0] + "B" * ii)
                                    pass

                                else:
                                    # print("A" * rect1[0] + "C" * iii)
                                    pass
                            return
                rect1 = recta.copy()
                rect2 = rectb.copy()
                rect3 = rectc.copy()

    # print(-1)
    pass


def main(n):
    # 根据规模 n 生成测试数据
    # 这里简单构造使三块可以拼成一个 n x n 的正方形:
    # A: n x 1, B: n x 1, C: n x (n-2)，对应输入为 (n,1,n,1,n,n-2)
    # 注意当 n < 3 时，有可能无法构造有效情况，这里仍然直接给出参数
    x1, y1 = n, 1
    x2, y2 = n, 1
    x3, y3 = n, max(1, n - 2)  # 保证边长为正

    func(x1, y1, x2, y2, x3, y3)