def main(n):
    # 映射规则：
    # N = max(1, min(n, 10))  控制规模在 1~10 范围用于实验
    # A = max(1, (n % 4) + 1) -> 1~4
    # B = max(1, (n % 4) + 1) 的一个确定性变换 -> 1~4
    if n <= 0:
        N = 1

    else:
        N = n if n <= 10 else 10

    A = (n % 4) + 1
    B = ((n * 2) % 4) + 1

    if N == 1:
        # print("YES")
        pass
        # print(0)
        pass
    elif N == 2:
        if A == 1 and B == 2:
            # print("YES")
            pass
            # print("01")
            pass
            # print("10")
            pass
        elif A == 2 and B == 1:
            # print("YES")
            pass
            # print("00")
            pass
            # print("00")
            pass

        else:
            # print("NO")
            pass
    elif N == 3:
        if A == 1 and B == 2:
            # print("YES")
            pass
            # print("011")
            pass
            # print("100")
            pass
            # print("100")
            pass
        elif A == 2 and B == 1:
            # print("YES")
            pass
            # print("001")
            pass
            # print("000")
            pass
            # print("100")
            pass
        elif A == 1 and B == 3:
            # print("YES")
            pass
            # print("011")
            pass
            # print("101")
            pass
            # print("110")
            pass
        elif A == 3 and B == 1:
            # print("YES")
            pass
            # print("000")
            pass
            # print("000")
            pass
            # print("000")
            pass

        else:
            # print("NO")
            pass

    else:
        if A != 1 and B != 1:
            # print("NO")
            pass

        else:
            # print("YES")
            pass

            if B == 1 and A != 1:
                mat = []
                for i in range(N):
                    if i == 0:
                        vec = []
                        for j in range(N):
                            if j >= A:
                                vec.append(1)

                            else:
                                vec.append(0)
                        mat.append(vec)

                    else:
                        vec = [0] * N
                        if i >= A:
                            vec[0] = 1
                        mat.append(vec)

                for idx in range(N):
                    # print("".join(list(map(str, mat[idx]))))
                    pass
            elif A == 1 and B != 1:
                mat = []
                for i in range(N):
                    if i == 0:
                        vec = []
                        for j in range(N):
                            if j >= B:
                                vec.append(0)

                            else:
                                vec.append(1)
                        vec[i] = 0
                        mat.append(vec)

                    else:
                        vec = [1] * N
                        if i >= B:
                            vec[0] = 0
                        vec[i] = 0
                        mat.append(vec)

                for idx in range(N):
                    # print("".join(list(map(str, mat[idx]))))
                    pass
            else:  # A == 1 and B == 1
                mat = []
                for i in range(N):
                    if i == 0:
                        vec = []
                        for j in range(N):
                            if j >= 2:
                                vec.append(1)

                            else:
                                vec.append(0)
                        mat.append(vec)

                    else:
                        vec = [0] * N
                        if i >= 2:
                            vec[0] = 1
                        mat.append(vec)

                if N > 2:
                    mat[1][2] = 1
                    mat[2][1] = 1
                for idx in range(N):
                    # print("".join(list(map(str, mat[idx]))))
                    pass
if __name__ == "__main__":
    main(5)