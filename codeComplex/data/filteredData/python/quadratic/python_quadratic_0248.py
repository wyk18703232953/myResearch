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
        print("YES")
        print(0)

    elif N == 2:
        if A == 1 and B == 2:
            print("YES")
            print("01")
            print("10")
        elif A == 2 and B == 1:
            print("YES")
            print("00")
            print("00")
        else:
            print("NO")

    elif N == 3:
        if A == 1 and B == 2:
            print("YES")
            print("011")
            print("100")
            print("100")
        elif A == 2 and B == 1:
            print("YES")
            print("001")
            print("000")
            print("100")
        elif A == 1 and B == 3:
            print("YES")
            print("011")
            print("101")
            print("110")
        elif A == 3 and B == 1:
            print("YES")
            print("000")
            print("000")
            print("000")
        else:
            print("NO")

    else:
        if A != 1 and B != 1:
            print("NO")
        else:
            print("YES")
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
                    print("".join(list(map(str, mat[idx]))))
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
                    print("".join(list(map(str, mat[idx]))))
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
                    print("".join(list(map(str, mat[idx]))))


if __name__ == "__main__":
    main(5)