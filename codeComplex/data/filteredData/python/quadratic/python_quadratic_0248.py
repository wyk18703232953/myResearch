import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里简单随机生成 A, B，范围 [1, max(3, n)]
    if n <= 0:
        return
    N = n
    limit = max(3, n)
    A = random.randint(1, limit)
    B = random.randint(1, limit)

    # 原逻辑开始
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

                for r in range(N):
                    print("".join(map(str, mat[r])))

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

                for r in range(N):
                    print("".join(map(str, mat[r])))

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

                mat[1][2] = 1
                mat[2][1] = 1
                for r in range(N):
                    print("".join(map(str, mat[r])))

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)